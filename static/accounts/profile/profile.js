//form edit and cancle button 
const editButton = document.querySelector(".edit-profile-btn");
const cancleButton = document.querySelector(".cancle");
const inputFields = document.querySelectorAll('.form-control');
const fileField = document.getElementById('file');


editButton.addEventListener("click", (event) => {
    event.preventDefault();
    inputFields.forEach(element => {
        element.removeAttribute("readonly")
        element.style.border = '2px solid #e6b89c';
        fileField.style.display = 'flex';
        editButton.style.display = 'none';
        cancleButton.style.display = 'unset';
    });
}
)

cancleButton.addEventListener("click", (event) => {
    event.preventDefault();
    inputFields.forEach(element => {
        element.setAttribute("readonly", 'true')
        element.style.border = '2px solid transparent';
        fileField.style.display = 'none';
        cancleButton.style.display = 'none';
        editButton.style.display = 'unset';
    });
}
)


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