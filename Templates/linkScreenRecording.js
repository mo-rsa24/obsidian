/**
 * LinkScreenRecording - Templater User Script
 *
 * Place this file in your Templater scripts folder
 * (configured in Templater settings under "Script files folder location")
 *
 * Usage: Run LinkScreenRecording.md template on selected text. 
 * It will first try to get a video from the clipboard. If none is found,
 * it will look for the latest video file in your system's video folders
 * and in your vault.
 */

async function linkScreenRecording(tp, app) {
    try {
        const { vault, workspace, fileManager } = app;
        const activeFile = workspace.getActiveFile();

        if (!activeFile) {
            return { success: false, error: "No active file" };
        }

        const editor = workspace.activeLeaf?.view?.editor;
        if (!editor) {
            return { success: false, error: "No active editor" };
        }

        const selection = editor.getSelection();
        if (!selection || selection.trim() === "") {
            return { success: false, error: "No text selected. Please highlight text first." };
        }

        const label = selection.trim();

        const selectionRange = {
            from: editor.getCursor('from'),
            to: editor.getCursor('to')
        };

        const type = await tp.system.prompt("Type (e.g., Demo)");
        if (!type) {
            return { success: false, error: "Type is required" };
        }

        const recordingResult = await getVideoAndMove(
            vault,
            fileManager,
            activeFile,
            label,
            app
        );

        if (!recordingResult.success) {
            return recordingResult;
        }

        const { videoPath, fileName } = recordingResult;

        const tocId = `toc-${generateUniqueId()}`;
        const refId = `ref-${generateUniqueId()}`;

        const contentLine = `[[${videoPath}|${label}]] [[#^${tocId}|↑]] ^${refId}`;

        await updateTOCAndContent(vault, activeFile, type, fileName, label, refId, tocId, selectionRange, contentLine, editor);

        return { success: true };

    } catch (error) {
        console.error("LinkScreenRecording error:", error);
        return { success: false, error: error.message };
    }
}

async function getVideoFromClipboard(vault, fileManager, currentFile, label) {
    try {
        const clipboardItems = await navigator.clipboard.read();
        let videoBlob = null;
        let extension = '';

        for (const item of clipboardItems) {
            const videoType = item.types.find(t => t.startsWith('video/'));
            if (videoType) {
                videoBlob = await item.getType(videoType);
                extension = videoType.split('/')[1];
                break;
            }
        }

        if (!videoBlob) {
            return { success: false, error: "No video found on the clipboard." };
        }
        
        const sanitizedLabel = sanitizeFilename(label);
        const newFileName = `${sanitizedLabel}.${extension}`;
        const outputsFolder = `${currentFile.parent ? currentFile.parent.path + "/" : ""}outputs`;
        
        try {
            const existingFolder = vault.getAbstractFileByPath(outputsFolder);
            if (!existingFolder) {
                await vault.createFolder(outputsFolder);
            }
        } catch (e) {
            // Folder might already exist
        }

        let finalPath = `${outputsFolder}/${newFileName}`;
        let counter = 1;
        while (vault.getAbstractFileByPath(finalPath)) {
            finalPath = `${outputsFolder}/${sanitizedLabel}-${counter}.${extension}`;
            counter++;
        }

        const arrayBuffer = await videoBlob.arrayBuffer();
        await vault.createBinary(finalPath, arrayBuffer);
        
        const relativePath = `outputs/${finalPath.split('/').pop()}`;

        return {
            success: true,
            videoPath: relativePath,
            fileName: finalPath.split('/').pop()
        };

    } catch (err) {
        console.warn("Could not read video from clipboard:", err.message);
        return { success: false, error: "Could not read video from clipboard." };
    }
}

async function getVideoAndMove(vault, fileManager, currentFile, label, app) {
    // First, try to get video from clipboard
    const clipboardResult = await getVideoFromClipboard(vault, fileManager, currentFile, label);
    if (clipboardResult.success) {
        new Notice("Used video from clipboard.");
        return clipboardResult;
    }

    // If clipboard fails, fall back to finding the latest file
    new Notice("No video on clipboard, searching files...");
    return findAndMoveLatestScreenRecording(vault, fileManager, currentFile, label);
}


/**
 * Find the most recent screen recording from file system and move it.
 */
async function findAndMoveLatestScreenRecording(vault, fileManager, currentFile, label) {
    const fs = require('fs');
    const path = require('path');

    let latestVideo = null;
    let latestTime = 0;
    let isExternal = false;
    let externalPath = null;

    const videoExtensions = ['mp4', 'webm', 'mov'];

    // 1. CHECK WINDOWS VIDEOS/CAPTURES FOLDER (external to vault)
    try {
        const userProfile = process.env.USERPROFILE || process.env.HOME;
        const videoFolders = [
            path.join(userProfile, 'Videos', 'Captures'),
            path.join(userProfile, 'Videos')
        ];

        for (const folder of videoFolders) {
            if (fs.existsSync(folder)) {
                const files = fs.readdirSync(folder);

                for (const filename of files) {
                    const ext = path.extname(filename).toLowerCase().substring(1);
                    if (videoExtensions.includes(ext)) {
                        const fullPath = path.join(folder, filename);
                        const stat = fs.statSync(fullPath);
                        const fileTime = stat.mtimeMs;

                        if (fileTime > latestTime) {
                            latestTime = fileTime;
                            latestVideo = { name: filename, extension: ext };
                            isExternal = true;
                            externalPath = fullPath;
                        }
                    }
                }
            }
        }
    } catch (e) {
        console.log("Could not access Windows Videos folder:", e.message);
    }

    // 2. CHECK IN-VAULT FOLDERS
    const vaultVideoFolders = [ "Videos", "Attachments", "Files", "" ];

    for (const folder of vaultVideoFolders) {
        const folderPath = folder === "" ? "/" : folder;
        const abstractFolder = vault.getAbstractFileByPath(folderPath);

        if (!abstractFolder || abstractFolder.children === undefined) continue;

        for (const file of abstractFolder.children) {
            if (file.extension && videoExtensions.includes(file.extension.toLowerCase())) {
                const stat = await vault.adapter.stat(file.path);
                const fileTime = stat?.mtime || 0;

                if (fileTime > latestTime) {
                    latestTime = fileTime;
                    latestVideo = file;
                    isExternal = false;
                    externalPath = null;
                }
            }
        }
    }
    
    const currentFolder = currentFile.parent;
    if (currentFolder) {
        for (const file of currentFolder.children) {
            if (file.extension && videoExtensions.includes(file.extension.toLowerCase())) {
                const stat = await vault.adapter.stat(file.path);
                const fileTime = stat?.mtime || 0;

                if (fileTime > latestTime) {
                    latestTime = fileTime;
                    latestVideo = file;
                    isExternal = false;
                    externalPath = null;
                }
            }
        }
    }

    if (!latestVideo) {
        return { success: false, error: "No recent screen recording found in Windows Videos/Captures or vault folders" };
    }

    const outputsFolder = `${currentFile.parent ? currentFile.parent.path + "/" : ""}outputs`;

    try {
        if (!await vault.adapter.exists(outputsFolder)) {
            await vault.createFolder(outputsFolder);
        }
    } catch (e) { /* Folder might already exist */ } 

    const sanitizedLabel = sanitizeFilename(label);
    const extension = latestVideo.extension;
    const newFileName = `${sanitizedLabel}.${extension}`;
    const newPath = `${outputsFolder}/${newFileName}`;

    let finalPath = newPath;
    let counter = 1;
    while (vault.getAbstractFileByPath(finalPath)) {
        finalPath = `${outputsFolder}/${sanitizedLabel}-${counter}.${extension}`;
        counter++;
    }

    if (isExternal) {
        const fs = require('fs');
        const fileBuffer = fs.readFileSync(externalPath);
        await vault.adapter.writeBinary(finalPath, fileBuffer);
    } else {
        await fileManager.renameFile(latestVideo, finalPath);
    }

    const relativePath = `outputs/${finalPath.split('/').pop()}`;

    return {
        success: true,
        videoPath: relativePath,
        fileName: finalPath.split('/').pop()
    };
}


function sanitizeFilename(name) {
    return name
        .replace(/["'/\\:*?<>|#\[\]]/g, '')
        .replace(/\s+/g, ' ')
        .trim()
        .substring(0, 100);
}

function generateUniqueId() {
    return Math.random().toString(36).substring(2, 9);
}

async function updateTOCAndContent(vault, file, type, fileName, label, refId, tocId, selectionRange, contentLine, editor) {
    let content = editor.getValue();
    const lines = content.split('\n');

    let tocIndex = -1;
    let tocEndIndex = -1;

    for (let i = 0; i < lines.length; i++) {
        if (lines[i].match(/^##\s+TOC\s*$/)) {
            tocIndex = i;
            for (let j = i + 1; j < lines.length; j++) {
                if (lines[j].match(/^#{1,6}\s/)) {
                    tocEndIndex = j - 1;
                    break;
                }
            }
            if (tocEndIndex === -1) tocEndIndex = lines.length - 1;
            break;
        }
    }

    const tocEntry = `- [[outputs/${fileName}|${type}]] : [[#^${refId}| ${label}]] ^${tocId}`;

    let tocInsertLine = 0;
    let linesAdded = 0;

    if (tocIndex === -1) {
        let insertIndex = 0;
        if (lines[0] === '---') {
            for (let i = 1; i < lines.length; i++) {
                if (lines[i] === '---') {
                    insertIndex = i + 1;
                    break;
                }
            }
        }
        while (insertIndex < lines.length && lines[insertIndex].trim() === '') {
            insertIndex++;
        }
        tocInsertLine = insertIndex;
        linesAdded = 4;
        lines.splice(insertIndex, 0, '## TOC', '', tocEntry, '');
    } else {
        let insertPos = tocEndIndex;
        while (insertPos > tocIndex && lines[insertPos].trim() === '') {
            insertPos--;
        }
        tocInsertLine = insertPos + 1;
        linesAdded = 1;
        lines.splice(insertPos + 1, 0, tocEntry);
    }

    let fromLine = selectionRange.from.line;
    let toLine = selectionRange.to.line;

    if (tocInsertLine <= fromLine) {
        fromLine += linesAdded;
        toLine += linesAdded;
    }

    const fromCh = selectionRange.from.ch;
    const toCh = selectionRange.to.ch;

    if (fromLine === toLine) {
        const line = lines[fromLine];
        lines[fromLine] = line.substring(0, fromCh) + contentLine + line.substring(toCh);
    } else {
        const firstLine = lines[fromLine].substring(0, fromCh);
        const lastLine = lines[toLine].substring(toCh);
        lines.splice(fromLine, toLine - fromLine + 1, firstLine + contentLine + lastLine);
    }

    editor.setValue(lines.join('\n'));
}

module.exports = linkScreenRecording;
