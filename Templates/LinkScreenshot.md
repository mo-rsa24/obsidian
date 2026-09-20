<%*
// LinkScreenshot Template
// Run this on selected text to capture a screenshot reference

const result = await tp.user.linkScreenshot(tp, this.app);

if (result && result.success) {
    // The script handles everything including cursor replacement
    // This template intentionally outputs nothing visible
    tR = "";
} else {
    tR = result?.error || "Failed to process screenshot link";
}
%>
