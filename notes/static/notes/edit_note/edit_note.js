
// Image preview functionality
const imageInput = document.getElementById("note-image");
const imagePreview = document.getElementById("image-preview");
const fileNameDisplay = document.getElementById("file-name");

imageInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        fileNameDisplay.textContent = file.name;

        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
        };
        reader.readAsDataURL(file);
    } else {
        fileNameDisplay.textContent = "No file chosen";
        imagePreview.innerHTML =
            '<span class="image-preview-placeholder">Image preview will appear here</span>';
    }
});


// Tag functionality
const tagInput = document.getElementById("tag-input-field");
const tagContainer = document.querySelector(".tag-input");

tagInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === ",") {
        e.preventDefault();
        addTag(this.value.trim());
        this.value = "";
    }
});

document.querySelectorAll(".tag-remove").forEach((btn) => {
    btn.addEventListener("click", function () {
        this.parentElement.remove();
    });
});

function addTag(text) {
    if (text === ""){
        return;

    }else{
        const tag = document.createElement("div");
        tag.className = "tag";
        tag.innerHTML = `${text}
         <button type="button" class="tag-remove">&times;</button>
         <input type="hidden" name="tags" value="${text}">`;

        tag.querySelector(".tag-remove").addEventListener("click", function () {
            tag.remove();
        });

        tagContainer.insertBefore(tag, tagInput);
    } 
     
}
