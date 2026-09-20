/**
 * Templater User Script — Download YouTube Clip
 *
 * Downloads a clipped segment of a YouTube video via yt-dlp and replaces the
 * highlighted text in the active note with a markdown link to the saved file.
 *
 * ── Prerequisites ──────────────────────────────────────────────────────────
 *   • yt-dlp  — on PATH  (https://github.com/yt-dlp/yt-dlp)
 *   • ffmpeg  — on PATH  (required by yt-dlp for clipping / merging)
 *
 * ── Setup ──────────────────────────────────────────────────────────────────
 *   1. Place this .js file in your Templater "User Script Functions" folder
 *      (Templater → Settings → User Script Functions folder).
 *   2. Create a template .md file (e.g. Templates/downloadYouTubeClip.md)
 *      with the single line:
 *          <% tp.user.downloadYouTubeClip(tp) -%>
 *   3. Bind that template to a hotkey:
 *        Templater → Settings → Template Hotkeys → Add
 *   4. Highlight text in a note, press the hotkey, follow the three prompts.
 *
 * ── Behaviour ──────────────────────────────────────────────────────────────
 *   • Prompts for: YouTube URL, start time, end time
 *   • Downloads only the specified segment (ffmpeg-based, no full download)
 *   • Saves to:  <NoteDir>/outputs/<SanitizedSelection>.mp4
 *   • Replaces the selection with: [original text](./relative/path.mp4)
 *   • Cancelling any prompt aborts without changes
 *
 * ── Cross-platform notes ───────────────────────────────────────────────────
 *   This script uses child_process.spawn (no shell) so that special
 *   characters in URLs and file paths are never interpreted by a shell.
 *   On Windows yt-dlp must be an .exe on PATH (the default for pip /
 *   winget / standalone installs).  macOS and Linux work out of the box.
 */

async function downloadYouTubeClip(tp) {
    const path   = require("path");
    const fs     = require("fs");
    const { spawn } = require("child_process");

    // ── Helpers ─────────────────────────────────────────────────────

    /**
     * Spawn a process and return a promise that resolves with stdout on
     * exit code 0, or rejects with the stderr / error message otherwise.
     * No shell is used — arguments are passed directly to the executable,
     * avoiding all escaping issues with URLs, paths, and glob characters.
     */
    function run(cmd, args) {
        return new Promise((resolve, reject) => {
            const proc = spawn(cmd, args, {
                stdio: "pipe",
                windowsHide: true,
            });
            let stdout = "";
            let stderr = "";
            proc.stdout.on("data", (d) => (stdout += d));
            proc.stderr.on("data", (d) => (stderr += d));
            proc.on("error", (err) => {
                if (err.code === "ENOENT") {
                    reject(
                        new Error(
                            `"${cmd}" not found. Make sure it is installed and on your PATH.`
                        )
                    );
                } else {
                    reject(err);
                }
            });
            proc.on("close", (code) => {
                if (code === 0) resolve(stdout);
                else
                    reject(
                        new Error(
                            stderr.trim() || `${cmd} exited with code ${code}`
                        )
                    );
            });
        });
    }

    /** Turn arbitrary text into a safe filename (no path separators, no
     *  reserved characters, collapsed whitespace → underscores). */
    function sanitizeFilename(name) {
        return (
            name
                .replace(/[<>:"/\\|?*\x00-\x1F]/g, "_")
                .replace(/\s+/g, "_")
                .replace(/_+/g, "_")
                .replace(/^_|_$/g, "")
                .substring(0, 100) || "clip"
        );
    }

    /** Return true when ts matches MM:SS or HH:MM:SS. */
    function isValidTimestamp(ts) {
        return /^(?:\d{1,2}:)?\d{1,2}:\d{2}$/.test(ts);
    }

    // ── 0. Get the current selection ────────────────────────────────

    const editor = app.workspace.activeLeaf?.view?.editor;
    if (!editor) {
        new Notice("No active editor.");
        return "";
    }

    const selection = editor.getSelection();
    if (!selection || !selection.trim()) {
        new Notice("No text highlighted — select some text first.");
        return "";
    }

    // ── 1. Three sequential prompts ─────────────────────────────────

    const url = await tp.system.prompt("YouTube URL");
    if (url == null || !url.trim()) return selection; // cancelled

    const startRaw = await tp.system.prompt("Start time (MM:SS or HH:MM:SS)");
    if (startRaw == null || !startRaw.trim()) return selection;

    const endRaw = await tp.system.prompt("End time (MM:SS or HH:MM:SS)");
    if (endRaw == null || !endRaw.trim()) return selection;

    const start = startRaw.trim();
    const end   = endRaw.trim();

    if (!isValidTimestamp(start) || !isValidTimestamp(end)) {
        new Notice("Invalid time format. Use MM:SS or HH:MM:SS.");
        return selection;
    }

    // ── 2. Resolve output paths ─────────────────────────────────────

    const activeFile = app.workspace.getActiveFile();
    if (!activeFile) {
        new Notice("No active file.");
        return selection;
    }

    const vaultBase = app.vault.adapter.basePath;
    const noteDir   = activeFile.parent?.path || "";

    // Output folder is <NoteDir>/outputs/  (sibling to the note)
    const outputsDirRel = noteDir
        ? path.join(noteDir, "outputs")
        : "outputs";
    const outputsDirAbs = path.join(vaultBase, outputsDirRel);

    // Create directory tree if it doesn't exist
    fs.mkdirSync(outputsDirAbs, { recursive: true });

    const safeName  = sanitizeFilename(selection);
    const filename  = `${safeName}.mp4`;
    const outputAbs = path.join(outputsDirAbs, filename);

    // Remove a previous file with the same name so yt-dlp doesn't skip
    if (fs.existsSync(outputAbs)) {
        fs.unlinkSync(outputAbs);
    }

    // ── 3. Download the clip via yt-dlp ─────────────────────────────

    const notice = new Notice(`Downloading clip (${start} → ${end})…`, 0);

    const ytdlpArgs = [
        "--download-sections", `*${start}-${end}`,
        "--force-keyframes-at-cuts",
        "-f", "bv*+ba/b",
        "--merge-output-format", "mp4",
        "--remux-video", "mp4",
        "--no-playlist",
        "--no-warnings",
        "-o", outputAbs,
        url.trim(),
    ];

    try {
        await run("yt-dlp", ytdlpArgs);
    } catch (err) {
        notice.hide();
        new Notice(`Download failed:\n${err.message}`, 15000);
        console.error("[downloadYouTubeClip]", err);
        return selection;
    }

    notice.hide();

    // ── 4. Verify the file landed ───────────────────────────────────

    if (!fs.existsSync(outputAbs)) {
        new Notice(
            "yt-dlp finished but the output file was not found.",
            10000
        );
        return selection;
    }

    // ── 5. Build a relative markdown link ───────────────────────────
    //
    // Path is relative to the note's own directory:
    //   ./outputs/<filename>.mp4
    //
    // encodeURI keeps forward-slashes intact but percent-encodes spaces
    // and other characters that are unsafe in markdown link targets.

    const linkPath = encodeURI(`./outputs/${filename}`);

    new Notice(`Clip saved: ${filename}`, 5000);

    // Returning the link causes Templater to replace the selection
    return `[${selection}](${linkPath})`;
}

module.exports = downloadYouTubeClip;
