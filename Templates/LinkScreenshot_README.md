# LinkScreenshot - Templater Template

Automatically capture screenshot references with bidirectional TOC linking in Obsidian.

## What It Does

When you run this template on **selected text**, it will:

1. ✅ Capture your selection as the label
2. ✅ Prompt you for a "Type" (e.g., `React`, `Bug`, `Feature`)
3. ✅ Find the most recent screenshot in your vault
4. ✅ Move it to `./outputs/` folder in your current note's directory
5. ✅ Rename it to match your label (sanitized)
6. ✅ Create/update a TOC section with a new entry
7. ✅ Replace your selection with a bidirectional link

## Setup Instructions

### 1. Configure Templater Scripts Folder

1. Open Obsidian Settings → Templater
2. Find **"Script files folder location"**
3. Set it to: `Templates` (or wherever these files are)
4. Click the folder icon to confirm the path

### 2. File Locations

Ensure these files are in your Templates folder:

- `LinkScreenshot.md` - The template file
- `linkScreenshot.js` - The user script
- `LinkScreenshot_README.md` - This file

### 3. Screenshot Sources

The script automatically searches for the **most recent screenshot** in these locations:

**Windows Screenshots (Primary):**
- `C:\Users\YourName\Pictures\Screenshots` - Windows native screenshots (Win+Shift+S, Win+PrtScn)

**In-Vault Folders (Fallback):**
- `Screenshots/`
- `Attachments/`
- `Images/`
- `Pasted/`
- Root folder `/`
- Current note's folder

**How it works:**
- Takes a **copy** from Windows Screenshots folder (original remains)
- **Moves** files from in-vault folders (cleans up as it goes)
- Always picks the **most recently modified** image across all locations

**To add custom folders:** Edit [linkScreenshot.js](linkScreenshot.js) and modify the `screenshotFolders` array.

## Usage

### Step-by-Step

1. **Take a Windows screenshot** using:
   - `Win + Shift + S` (Snipping Tool)
   - `Win + PrtScn` (Full screen)
   - Or paste into Obsidian (will use vault folder)
2. **Highlight/select text** in your note that describes the screenshot
   - Example: Select `User Login Flow` or `Navigation Menu Bug`
3. **Run the template:**
   - Command Palette (`Ctrl + P`) → `Templater: Insert Template`
   - Choose `LinkScreenshot`
   - OR assign a hotkey to this template
4. **Enter a Type** when prompted (e.g., `React`, `Design`, `Bug`)
5. ✨ Done! The screenshot is copied into your note's `outputs/` folder

### What Gets Created

#### In the TOC (auto-created near top of note):

```markdown
## TOC

- [[outputs/User Login Flow.png|React]] : [[#^ref-abc123| User Login Flow]] ^toc-xyz789
```

#### At your cursor (replaces selection):

```markdown
[[outputs/User Login Flow.png|User Login Flow]] [[#^toc-xyz789|↑]] ^ref-abc123
```

### Bidirectional Navigation

- **Click the Type (React) in TOC** → Opens the image
- **Click the label in TOC** → Jumps down to the content location (`^ref-abc123`)
- **Click `↑` in content** → Jumps back up to TOC (`^toc-xyz789`)
- **Click the label in content** → Opens the image

## File Organization

```
Your Note Folder/
├── YourNote.md
└── outputs/
    ├── User Login Flow.png
    ├── Navigation Menu Bug.png
    └── Dashboard Layout.png
```

The `outputs/` folder is created automatically if it doesn't exist.

## Filename Sanitization

Labels are automatically cleaned for filesystem safety:

- **Invalid characters removed:** `/ \ : * ? " < > | # [ ]`
- **Multiple spaces** → Single space
- **Trimmed** whitespace
- **Length limited** to 100 characters

Examples:
- `User: Login [v2]` → `User Login v2.png`
- `What's   new?` → `Whats new.png`

## Troubleshooting

### "No text selected" error

- Make sure you **highlight text** before running the template

### "No recent screenshot found in Windows Screenshots or vault folders" error

**First, verify your Windows Screenshots folder exists:**
1. Press `Win + R` → type `%USERPROFILE%\Pictures\Screenshots` → Enter
2. If it opens, you're good! If not, take a test screenshot with `Win + Shift + S`

**If the folder exists but still not working:**
- Make sure you took a screenshot **recently** (the script finds the newest one)
- Check file extensions are supported: `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`
- Try pasting a screenshot directly into Obsidian instead (it will search vault folders too)

**Custom screenshot location:**
If your screenshots are saved elsewhere, edit [linkScreenshot.js](linkScreenshot.js) around line 78 and change:
```javascript
const windowsScreenshotPath = path.join(userProfile, 'Pictures', 'Screenshots');
```
to your custom path.

### Template doesn't run / "linkScreenshot is not defined"

1. Verify the **Script files folder location** in Templater settings
2. Make sure `linkScreenshot.js` is in that folder
3. Try restarting Obsidian
4. Check the filename is exactly `linkScreenshot.js` (case-sensitive)

### TOC appears in wrong location

The script tries to:
1. Find existing `## TOC` heading
2. If not found, creates it after frontmatter
3. If no frontmatter, creates it at the top

**To force a location:** Manually add `## TOC` heading where you want it.

### Duplicate filenames

If a file with the same name exists in `outputs/`, a number suffix is added:
- `label.png` → `label-1.png` → `label-2.png`

## Customization

### Change TOC Heading

Edit [linkScreenshot.js:147](linkScreenshot.js#L147):

```javascript
if (lines[i].match(/^##\s+TOC\s*$/)) {
```

Change `TOC` to your preferred heading (e.g., `Screenshots`, `References`).

### Change Output Folder Name

Edit [linkScreenshot.js:102](linkScreenshot.js#L102):

```javascript
const outputsFolder = `${currentFile.parent ? currentFile.parent.path + "/" : ""}outputs`;
```

Change `outputs` to your preferred folder name.

### Modify Link Format

Edit the template in [linkScreenshot.js:263](linkScreenshot.js#L263) (TOC entry):

```javascript
const tocEntry = `- [[outputs/${fileName}|${type}]] : [[#^${refId}| ${label}]] ^${tocId}`;
```

And [linkScreenshot.js:60](linkScreenshot.js#L60) (content line):

```javascript
const contentLine = `[[${imagePath}|${label}]] [[#^${tocId}|↑]] ^${refId}`;
```

## Tips

- **Assign a hotkey** to this template for faster workflow
- **Use descriptive labels** - they become both the link text and filename
- **Consistent Types** - Use the same type labels (React, Bug, etc.) for better organization
- **Batch processing** - Take multiple screenshots, then annotate them all in sequence

## License

Free to use and modify for your personal vault.

---

**Questions or Issues?** Check the Templater documentation: https://silentvoid13.github.io/Templater/
