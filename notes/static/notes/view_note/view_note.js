const deleteButton = document.querySelector("#delete-btn");
const closeButton = document.querySelector(".cancel-btn");
const deleteForm = document.querySelector(".delete-form");

if (deleteButton) {
    deleteButton.addEventListener("click", () => {
        deleteForm.style.display = "flex";
    });

    closeButton.addEventListener("click", () => {
        deleteForm.style.display = "none";
    });
}

// Star button toggle
const starBtn = document.querySelector(".star-btn");

starBtn.addEventListener("click", () => {
    starBtn.classList.toggle("active");
    if (starBtn.classList.contains("active")) {
        starBtn.innerHTML = '<span class="button-icon">★</span> Bookmarked';
    } else {
        starBtn.innerHTML = '<span class="button-icon">★</span> Add to Bookmark';
    }
});

// like button toggle
const likeBtn = document.querySelector(".like-btn");

likeBtn.addEventListener("click", () => {
    likeBtn.classList.toggle("active");
    if (likeBtn.classList.contains("active")) {
        likeBtn.style.backgroundColor = "red";
        likeBtn.style.color = "white";
        likeBtn.innerHTML = '<span class="button-icon"><i class="fa-solid fa-heart"></i></span>';
    } else {
        likeBtn.style.backgroundColor = "unset";
        likeBtn.style.color = "red";
        likeBtn.innerHTML = '<span class="button-icon"><i class="fa-regular fa-heart"></i></span>';
    }
});


// Follow button toggle
const followBtn = document.querySelector(".follow-btn");

followBtn.addEventListener("click", () => {
    if (followBtn.textContent.includes("Follow")) {
        followBtn.innerHTML = '<span class="button-icon">✓</span> Following';
        followBtn.style.backgroundColor = "#4A4238";
    } else {
        followBtn.innerHTML = '<span class="button-icon">+</span> Follow';
        followBtn.style.backgroundColor = "";
    }
});
