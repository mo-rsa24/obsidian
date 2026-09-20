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
    new Notice("Please highlight some text first.");
    return;
}

const genId = () => Math.random().toString(36).substring(2, 7);

// Normalize and detect re-run
let cleanText = selection.trimEnd();
let existingNavId = null;
let existingBlockId = null;

// Re-run format: text [[#^nav-id|↑]] ^block-id
const rerunMatch = cleanText.match(/^([\s\S]*?)\s*\[\[#\^([a-z0-9-]+)\|↑\]\]\s*\^([a-z0-9-]+)$/i);

if (rerunMatch) {
    cleanText = rerunMatch[1];
    existingNavId = rerunMatch[2];
    existingBlockId = rerunMatch[3];
} else {
    // Partial: only a block ID present (no arrow yet)
    const blockOnly = cleanText.match(/^([\s\S]*?)\s*\^([a-z0-9-]+)$/i);
    if (blockOnly) {
        cleanText = blockOnly[1];
        existingBlockId = blockOnly[2];
    }
}

const blockId = existingBlockId || `ref-${genId()}`;
const navId = existingNavId || `nav-${genId()}`;
const label = cleanText.trim();

// Build updated content: original text + arrow link + block ID
const updatedSelection = `${cleanText} [[#^${navId}|↑]] ^${blockId}`;

// Build TOC entry
const tocEntry = `- [[#^${blockId}|${label}]] ^${navId}`;

// Replace selection in editor
editor.replaceSelection(updatedSelection);

// Update or create the highlights TOC
let fullContent = editor.getValue();
const tocHeader = "<!-- highlights:start -->";
const tocFooter = "<!-- highlights:end -->";
const tocRegex = /<!-- highlights:start -->([\s\S]*?)<!-- highlights:end -->/;
const tocMatch = fullContent.match(tocRegex);

if (tocMatch) {
    let tocBody = tocMatch[1];
    // Check if an entry for this blockId already exists
    const entryRegex = new RegExp(`^- \\[\\[#\\^${blockId}\\|[^\\]]*\\]\\].*$`, 'm');
    if (entryRegex.test(tocBody)) {
        // Update existing entry in place
        tocBody = tocBody.replace(entryRegex, tocEntry);
    } else {
        // Append new entry
        tocBody = tocBody.trimEnd() + '\n' + tocEntry + '\n';
    }
    fullContent = fullContent.replace(tocRegex, `${tocHeader}\n${tocBody.trim()}\n${tocFooter}`);
} else {
    // No highlights TOC exists, prepend to top of note
    fullContent = `${tocHeader}\n${tocEntry}\n${tocFooter}\n\n` + fullContent;
}

editor.setValue(fullContent);
new Notice("Highlight linked to TOC.");
%>
