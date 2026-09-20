<%*
// 1. Get the highlighted text
const selection = tp.file.selection();
if (!selection) {
    new Notice("Error: No text selected!");
    return;
}

// 2. Sanitize selection for filename (remove special characters)
const fileName = selection.replace(/[^a-z0-9]/gi, '_').toLowerCase() + "_" + Date.now();
const folderPath = tp.file.folder(true) + "/assets"

// 3. Ensure the 'assets' folder exists
if (!await app.vault.adapter.exists(folderPath)) {
    await app.vault.createFolder(folderPath);
}

// 4. Access the clipboard for the image
// Note: This uses the Obsidian internal paste command logic
const clipboardItems = await navigator.clipboard.read();
let imageBlob = null;

for (const item of clipboardItems) {
    if (item.types.includes("image/png")) {
        imageBlob = await item.getType("image/png");
        break;
    }
}

if (!imageBlob) {
    new Notice("Error: No image found in clipboard!");
    return;
}

// 5. Save the file to the vault
const arrayBuffer = await imageBlob.arrayBuffer();
const filePath = `${folderPath}/${fileName}.png`;
await app.vault.createBinary(filePath, arrayBuffer);

// 6. Output the Markdown link
const encodedFilePath = filePath.replace(/ /g, '%20');
tR += `[${selection}](${encodedFilePath})`;
%>