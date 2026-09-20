<%*
const { MarkdownView, Notice } = tp.obsidian;
const activeView = app.workspace.getActiveViewOfType(MarkdownView);

if (!activeView) {
    new Notice("No active Markdown view found.");
    return;
}

const editor = activeView.editor;
const selection = editor.getSelection();

if (!selection || !selection.trim()) {
    new Notice("Please highlight a line first.");
    return;
}

const genId = () => Math.random().toString(36).substring(2, 7);
let trimmed = selection.trimEnd();

// Check if line already has the colon-link format (re-run scenario)
let existingTocId = null;
let existingContentId = null;
const colonLinkMatch = trimmed.match(/^(.*?)\[\[#\^([a-z0-9-]+)\|:\]\](.*)$/i);
if (colonLinkMatch) {
    // Already processed - extract the IDs and normalize back to plain format
    existingTocId = colonLinkMatch[2];
    const beforeColon = colonLinkMatch[1].trimEnd();
    const afterColonLink = colonLinkMatch[3];

    // Check for content block ID
    const contentIdMatch = afterColonLink.match(/\s\^([a-z0-9-]+)$/i);
    if (contentIdMatch) {
        existingContentId = contentIdMatch[1];
    }

    // Reconstruct as plain text with colon
    trimmed = beforeColon + ':' + afterColonLink.replace(/\s\^[a-z0-9-]+$/i, '');
}

// Check for colon
const colonIndex = trimmed.indexOf(':');
if (colonIndex === -1) {
    new Notice("No colon found in selection.");
    return;
}

// Extract any leading indent / bullet marker
const indentMatch = trimmed.match(/^(\s*(?:[-*+]|\d+\.)\s*)/);
const indent = indentMatch ? indentMatch[1] : "";
const labelStart = indent.length;
const label = trimmed.substring(labelStart, colonIndex).trim();

// Generate or reuse IDs
const contentId = existingContentId || genId();  // ID for content line
const tocId = existingTocId || genId();  // ID for TOC entry

// Text after the colon - ensure we don't have any existing block IDs
let afterColon = trimmed.substring(colonIndex + 1).trim();
// Remove any existing block ID that might have slipped through
afterColon = afterColon.replace(/\s*\^[a-z0-9-]+\s*$/i, '').trim();

// Build the updated line with block ID absolutely at the end
let updatedLine;
if (afterColon) {
    updatedLine = `${indent}${label}[[#^${tocId}|:]] ${afterColon} ^${contentId}`;
} else {
    updatedLine = `${indent}${label}[[#^${tocId}|:]] ^${contentId}`;
}

// TOC entry with its own block ID for back-linking
const tocEntry = `- [[#^${contentId}|${label}]] ^${tocId}`;

// Get current position info before modifying content
const selectionStart = editor.getCursor('from');
const selectionEnd = editor.getCursor('to');

// Get full content and calculate positions
let fullContent = editor.getValue();
const beforePos = editor.posToOffset(selectionStart);
const afterPos = editor.posToOffset(selectionEnd);

// Replace the selection in fullContent
fullContent = fullContent.substring(0, beforePos) + updatedLine + fullContent.substring(afterPos);

// Update or create the line TOC
const tocHeader = "<!-- toc:line:start -->";
const tocFooter = "<!-- toc:line:end -->";
const tocRegex = /<!-- toc:line:start -->([\s\S]*?)<!-- toc:line:end -->/;
const tocMatch = fullContent.match(tocRegex);

if (tocMatch) {
    let tocBody = tocMatch[1];
    // Check if entry for this contentId already exists
    const entryRegex = new RegExp(`^.*\\[\\[#\\^${contentId}\\|[^\\]]*\\]\\].*$`, 'm');
    if (entryRegex.test(tocBody)) {
        // Update in place
        tocBody = tocBody.replace(entryRegex, tocEntry);
    } else {
        // Append new entry
        tocBody = tocBody.trimEnd() + '\n' + tocEntry + '\n';
    }
    fullContent = fullContent.replace(tocRegex, `${tocHeader}\n${tocBody.trim()}\n${tocFooter}`);
} else {
    // No line TOC exists yet — place after last TOC block, or at top
    const endMarkers = [...fullContent.matchAll(/<!-- (?:toc:auto|toc:line|highlights):end -->/g)];
    if (endMarkers.length > 0) {
        const last = endMarkers[endMarkers.length - 1];
        const insertPos = last.index + last[0].length;
        fullContent = fullContent.substring(0, insertPos)
            + `\n\n${tocHeader}\n${tocEntry}\n${tocFooter}`
            + fullContent.substring(insertPos);
    } else {
        fullContent = `${tocHeader}\n${tocEntry}\n${tocFooter}\n\n` + fullContent;
    }
}

editor.setValue(fullContent);
new Notice("Line linked to TOC.");
%>
