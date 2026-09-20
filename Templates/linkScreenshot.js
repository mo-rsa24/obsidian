/**
 * LinkScreenshot - Templater User Script
 *
 * Place this file in your Templater scripts folder
 * (configured in Templater settings under "Script files folder location")
 *
 * Usage: Run LinkScreenshot.md template on selected text
 */

async function linkScreenshot(tp, app) {
    try {
        const { vault, workspace, fileManager } = app;
        const activeFile = workspace.getActiveFile();

        if (!activeFile) {
            return { success: false, error: "No active file" };
        }

        // Get the editor and selection
        const editor = workspace.activeLeaf?.view?.editor;
        if (!editor) {
            return { success: false, error: "No active editor" };
        }

        const selection = editor.getSelection();
        if (!selection || selection.trim() === "") {
            return { success: false, error: "No text selected. Please highlight text first." };
        }

        const label = selection.trim();

        // Get selection range before any modifications
        const selectionRange = {
            from: editor.getCursor('from'),
            to: editor.getCursor('to')
        };

        // A) Prompt for Type
        const type = await tp.system.prompt("Type (e.g., React)");
        if (!type) {
            return { success: false, error: "Type is required" };
        }

        // B) Find and move the latest screenshot
        const screenshotResult = await findAndMoveLatestScreenshot(
            vault,
            fileManager,
            activeFile,
            label
        );

        if (!screenshotResult.success) {
            return screenshotResult;
        }

        const { imagePath, fileName } = screenshotResult;

        // C) Generate unique IDs for bidirectional linking
        const tocId = `toc-${generateUniqueId()}`;
        const refId = `ref-${generateUniqueId()}`;

        // Create content line replacement text
        const contentLine = `[[${imagePath}|${label}]] [[#^${tocId}|↑]] ^${refId}`;

        // Update TOC and replace selection in one operation
        await updateTOCAndContent(vault, activeFile, type, fileName, label, refId, tocId, selectionRange, contentLine, editor);

        return { success: true };

    } catch (error) {
        console.error("LinkScreenshot error:", error);
        return { success: false, error: error.message };
    }
}

/**
 * Find the most recent screenshot and move it to outputs folder
 */
async function findAndMoveLatestScreenshot(vault, fileManager, currentFile, label) {
    const fs = require('fs');
    const path = require('path');

    let latestImage = null;
    let latestTime = 0;
    let isExternal = false;
    let externalPath = null;

    // 1. CHECK WINDOWS SCREENSHOTS FOLDER (external to vault)
    try {
        const userProfile = process.env.USERPROFILE || process.env.HOME;
        const windowsScreenshotPath = path.join(userProfile, 'Pictures', 'Screenshots');

        if (fs.existsSync(windowsScreenshotPath)) {
            const files = fs.readdirSync(windowsScreenshotPath);

            for (const filename of files) {
                const ext = path.extname(filename).toLowerCase().substring(1);
                if (['png', 'jpg', 'jpeg', 'gif', 'webp'].includes(ext)) {
                    const fullPath = path.join(windowsScreenshotPath, filename);
                    const stat = fs.statSync(fullPath);
                    const fileTime = stat.mtimeMs;

                    if (fileTime > latestTime) {
                        latestTime = fileTime;
                        latestImage = { name: filename, extension: ext };
                        isExternal = true;
                        externalPath = fullPath;
                    }
                }
            }
        }
    } catch (e) {
        console.log("Could not access Windows Screenshots folder:", e.message);
    }

    // 2. CHECK IN-VAULT FOLDERS
    const screenshotFolders = [
        "Screenshots",
        "Attachments",
        "Images",
        "Pasted",
        "" // Root folder
    ];

    // Search for most recent image in vault
    for (const folder of screenshotFolders) {
        const folderPath = folder === "" ? "/" : folder;
        const abstractFolder = vault.getAbstractFileByPath(folderPath);

        if (!abstractFolder || abstractFolder.children === undefined) continue;

        for (const file of abstractFolder.children) {
            if (file.extension && ['png', 'jpg', 'jpeg', 'gif', 'webp'].includes(file.extension.toLowerCase())) {
                const stat = await vault.adapter.stat(file.path);
                const fileTime = stat?.mtime || 0;

                if (fileTime > latestTime) {
                    latestTime = fileTime;
                    latestImage = file;
                    isExternal = false;
                    externalPath = null;
                }
            }
        }
    }

    // Also check the current note's folder
    const currentFolder = currentFile.parent;
    if (currentFolder) {
        for (const file of currentFolder.children) {
            if (file.extension && ['png', 'jpg', 'jpeg', 'gif', 'webp'].includes(file.extension.toLowerCase())) {
                const stat = await vault.adapter.stat(file.path);
                const fileTime = stat?.mtime || 0;

                if (fileTime > latestTime) {
                    latestTime = fileTime;
                    latestImage = file;
                    isExternal = false;
                    externalPath = null;
                }
            }
        }
    }

    if (!latestImage) {
        return { success: false, error: "No recent screenshot found in Windows Screenshots or vault folders" };
    }

    // Create outputs folder if it doesn't exist
    const outputsFolder = `${currentFile.parent ? currentFile.parent.path + "/" : ""}outputs`;

    try {
        const existingFolder = vault.getAbstractFileByPath(outputsFolder);
        if (!existingFolder) {
            await vault.createFolder(outputsFolder);
        }
    } catch (e) {
        // Folder might already exist
    }

    // Sanitize label for filename
    const sanitizedLabel = sanitizeFilename(label);
    const extension = latestImage.extension;
    const newFileName = `${sanitizedLabel}.${extension}`;
    const newPath = `${outputsFolder}/${newFileName}`;

    // Check if file already exists, if so add number suffix
    let finalPath = newPath;
    let counter = 1;
    while (vault.getAbstractFileByPath(finalPath)) {
        finalPath = `${outputsFolder}/${sanitizedLabel}-${counter}.${extension}`;
        counter++;
    }

    // Handle external vs internal files differently
    if (isExternal) {
        // Copy from external location (e.g., Windows Screenshots) into vault
        const fs = require('fs');
        const fileBuffer = fs.readFileSync(externalPath);
        await vault.adapter.writeBinary(finalPath, fileBuffer);
    } else {
        // Move and rename within vault
        await fileManager.renameFile(latestImage, finalPath);
    }

    // Return relative path from current note
    const relativePath = `outputs/${finalPath.split('/').pop()}`;

    return {
        success: true,
        imagePath: relativePath,
        fileName: finalPath.split('/').pop()
    };
}

/**
 * Sanitize filename - remove invalid characters
 */
function sanitizeFilename(name) {
    return name
        .replace(/[\/\\:*?"<>|#\[\]]/g, '') // Remove invalid chars
        .replace(/\s+/g, ' ') // Collapse multiple spaces
        .trim()
        .substring(0, 100); // Limit length
}

/**
 * Generate a unique ID for block references
 */
function generateUniqueId() {
    return Math.random().toString(36).substring(2, 9);
}

/**
 * Update or create TOC section with new entry AND replace selection
 */
async function updateTOCAndContent(vault, file, type, fileName, label, refId, tocId, selectionRange, contentLine, editor) {
    let content = editor.getValue();
    const lines = content.split('\n');

    // Find or create TOC section
    let tocIndex = -1;
    let tocEndIndex = -1;

    for (let i = 0; i < lines.length; i++) {
        if (lines[i].match(/^##\s+TOC\s*$/)) {
            tocIndex = i;
            // Find the end of TOC section (next heading or end of file)
            for (let j = i + 1; j < lines.length; j++) {
                if (lines[j].match(/^#{1,6}\s/)) {
                    tocEndIndex = j - 1;
                    break;
                }
            }
            if (tocEndIndex === -1) {
                tocEndIndex = lines.length - 1;
            }
            break;
        }
    }

    // Create TOC entry with link to content block
    const tocEntry = `- [[outputs/${fileName}|${type}]] : [[#^${refId}| ${label}]] ^${tocId}`;

    // Track where TOC is inserted and how many lines are added
    let tocInsertLine = 0;
    let linesAdded = 0;

    if (tocIndex === -1) {
        // Create new TOC section at the top (after frontmatter if exists)
        let insertIndex = 0;

        // Skip frontmatter if it exists
        if (lines[0] === '---') {
            for (let i = 1; i < lines.length; i++) {
                if (lines[i] === '---') {
                    insertIndex = i + 1;
                    break;
                }
            }
        }

        // Skip empty lines
        while (insertIndex < lines.length && lines[insertIndex].trim() === '') {
            insertIndex++;
        }

        tocInsertLine = insertIndex;
        linesAdded = 4; // '## TOC', '', tocEntry, ''
        lines.splice(insertIndex, 0, '## TOC', '', tocEntry, '');
    } else {
        // Add to existing TOC section (at the end before next section)
        let insertPos = tocEndIndex;

        // Find last non-empty line in TOC
        while (insertPos > tocIndex && lines[insertPos].trim() === '') {
            insertPos--;
        }

        tocInsertLine = insertPos + 1;
        linesAdded = 1; // just tocEntry
        lines.splice(insertPos + 1, 0, tocEntry);
    }

    // Adjust selection range if TOC was inserted before it
    let fromLine = selectionRange.from.line;
    let toLine = selectionRange.to.line;

    if (tocInsertLine <= fromLine) {
        fromLine += linesAdded;
        toLine += linesAdded;
    }

    // Replace the selected text with content line
    const fromCh = selectionRange.from.ch;
    const toCh = selectionRange.to.ch;

    if (fromLine === toLine) {
        // Selection is on a single line
        const line = lines[fromLine];
        const before = line.substring(0, fromCh);
        const after = line.substring(toCh);
        lines[fromLine] = before + contentLine + after;
    } else {
        // Selection spans multiple lines
        const firstLine = lines[fromLine].substring(0, fromCh);
        const lastLine = lines[toLine].substring(toCh);
        lines.splice(fromLine, toLine - fromLine + 1, firstLine + contentLine + lastLine);
    }

    // Write back to file
    editor.setValue(lines.join('\n'));
}

module.exports = linkScreenshot;
