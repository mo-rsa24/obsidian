<%*
const { MarkdownView, Notice } = tp.obsidian;
const activeView = app.workspace.getActiveViewOfType(MarkdownView);

if (!activeView) {
    new Notice("No active Markdown view found.");
    return;
}

const editor = activeView.editor;
const selection = editor.getSelection();

if (!selection) {
    new Notice("Please select your bullet list first.");
    return;
}

// 1. Helper to generate unique ID
const genId = () => Math.random().toString(36).substring(2, 7);

// 2. Parse selection and build updates
const lines = selection.split('\n');
let tocLines = [];
let updatedLines = [];
let contentBlockIds = new Set();

lines.forEach(line => {
    let trimmed = line.trimEnd();

    // Normalize: strip any existing back-link format so we can re-parse cleanly
    let existingNavId = null;
    // Current format: label[[#^id|:]]rest
    const colonLinkMatch = trimmed.match(/^(\s*[-*+]\s*)(.+?)\[\[#\^([a-z0-9-]+)\|:\]\](.*)$/i);
    // Old format: [[#^id|label]]:rest
    const labelLinkMatch = !colonLinkMatch && trimmed.match(/^(\s*[-*+]\s*)\[\[#\^([a-z0-9-]+)\|(.+?)\]\]:(.*)$/i);

    if (colonLinkMatch) {
        existingNavId = colonLinkMatch[3];
        trimmed = `${colonLinkMatch[1]}${colonLinkMatch[2].trim()}:${colonLinkMatch[4]}`;
    } else if (labelLinkMatch) {
        existingNavId = labelLinkMatch[2];
        trimmed = `${labelLinkMatch[1]}${labelLinkMatch[3]}:${labelLinkMatch[4]}`;
    }

    const colonIndex = trimmed.indexOf(':');
    if (colonIndex === -1) {
        updatedLines.push(trimmed);
        return;
    }

    const indentMatch = trimmed.match(/^(\s*[-*+]\s*)/);
    const indent = indentMatch ? indentMatch[1] : "";
    const label = trimmed.substring(indent.length, colonIndex).trim();
    const navId = existingNavId || `nav-${genId()}`;

    // Check for existing content block ID
    let blockIdMatch = trimmed.match(/\s\^([a-z0-9-]+)$/i);
    let blockId = blockIdMatch ? blockIdMatch[1] : `toc-${genId()}`;

    contentBlockIds.add(blockId);

    // Text after the colon (without the colon itself), stripping any block ID
    let afterColon = trimmed.substring(colonIndex + 1);
    if (blockIdMatch) {
        afterColon = afterColon.replace(/\s\^[a-z0-9-]+$/i, '');
    }

    // Content line: the colon is the clickable link back to the TOC entry
    updatedLines.push(`${indent}${label}[[#^${navId}|:]]${afterColon} ^${blockId}`);

    // TOC line: links to content block ID, carries its own nav block ID
    const tocIndent = indent.replace(/[*+]/, '-');
    tocLines.push(`${tocIndent}[[#^${blockId}|${label}]] ^${navId}`);
});

// 3. Construct the TOC block
const tocHeader = "<!-- toc:auto:start -->";
const tocFooter = "<!-- toc:auto:end -->";
const newTocContent = `${tocHeader}\n${tocLines.join('\n')}\n${tocFooter}`;

// 4. Replace selection with block-ID-annotated lines
editor.replaceSelection(updatedLines.join('\n'));

// 5. Update or insert the TOC
let fullContent = editor.getValue();
const tocBlockRegex = /<!-- toc:auto:start -->[\s\S]*?<!-- toc:auto:end -->/g;
const matches = [...fullContent.matchAll(tocBlockRegex)];

// Find the TOC block that shares block IDs with this selection
let matchingMatch = null;
for (const match of matches) {
    for (const id of contentBlockIds) {
        if (match[0].includes(id)) {
            matchingMatch = match;
            break;
        }
    }
    if (matchingMatch) break;
}

if (matchingMatch) {
    // Re-run: replace the matching TOC block in place
    fullContent = fullContent.substring(0, matchingMatch.index)
        + newTocContent
        + fullContent.substring(matchingMatch.index + matchingMatch[0].length);
} else if (matches.length > 0) {
    // New selection: append after the last existing TOC block
    const last = matches[matches.length - 1];
    const insertPos = last.index + last[0].length;
    fullContent = fullContent.substring(0, insertPos)
        + "\n\n" + newTocContent
        + fullContent.substring(insertPos);
} else {
    // No TOC blocks at all: prepend to top
    fullContent = newTocContent + "\n\n" + fullContent;
}

editor.setValue(fullContent);
new Notice("TOC synchronized successfully.");
%>