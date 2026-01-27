document.addEventListener("DOMContentLoaded", () => {
    const uploadBox = document.querySelector(".upload-box");
    const fileInput = document.querySelector("#profile_image");

    if (!uploadBox || !fileInput) return;

    // Highlight when dragging over
    uploadBox.addEventListener("dragover", (e) => {
        e.preventDefault();
        uploadBox.classList.add("drag-over");
    });

    // Remove highlight when leaving
    uploadBox.addEventListener("dragleave", () => {
        uploadBox.classList.remove("drag-over");
    });

    // Handle drop
    uploadBox.addEventListener("drop", (e) => {
        e.preventDefault();
        uploadBox.classList.remove("drag-over");

        if (e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
            updateText(e.dataTransfer.files[0].name);
        }
    });

    // Handle click upload
    fileInput.addEventListener("change", () => {
        if (fileInput.files.length > 0) {
            updateText(fileInput.files[0].name);
        }
    });

    function updateText(filename) {
        const text = uploadBox.querySelector(".upload-text");
        text.innerHTML = `Selected file:<br><strong>${filename}</strong>`;
    }
});
