module.exports = async (params) => {
  const app = params.app;
  const { MarkdownView, Notice } = require("obsidian");

  const view = app.workspace.getActiveViewOfType(MarkdownView);
  if (!view) return new Notice("No active markdown editor");

  const editor = view.editor;
  const selection = editor.getSelection();
  if (!selection) return new Notice("Select text first");

  const file = view.file;
  const folder = file.parent.path;
  const assetsPath = `${folder}/assets`;
  const fs = app.vault.adapter;

  if (!(await fs.exists(assetsPath))) await fs.mkdir(assetsPath);

  const list = await fs.list(assetsPath);
  const imgs = list.files
    .filter(f => f.match(/\.(png|jpg|jpeg)$/i))
    .sort((a, b) => fs.stat(b).mtime - fs.stat(a).mtime);

  if (!imgs.length) return new Notice("No image found in current note’s assets/");

  const latest = imgs[0];

  const safeName = selection
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");

  const newPath = `${assetsPath}/${safeName}.png`;

  await fs.rename(latest, newPath);
  editor.replaceSelection(`[[assets/${safeName}.png|${selection}]]`);
};
