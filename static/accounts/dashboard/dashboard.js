// Toggle mobile sidebar
const mobileToggle = document.querySelector(".mobile-sidebar-toggle");
const dashboardSidebar = document.querySelector(".dashboard-sidebar");

mobileToggle.addEventListener("click", () => {
    dashboardSidebar.classList.toggle("active");
    window.scrollTo({
        top: 0,
        behavior: "smooth", 
    });
});


const sidebarButtons = document.querySelectorAll(".sidebar-btn");

sidebarButtons.forEach((button) => {
    button.addEventListener("click", function () {
        sidebarButtons.forEach((btn) => btn.classList.remove("active"));

        document.querySelectorAll(".content-type").forEach((el) => {
            el.classList.add("hidden-box");
        });

        const targetId = `${button.id}-box`;
        const targetElement = document.getElementById(targetId);

        if (targetElement) targetElement.classList.remove("hidden-box");

        this.classList.add("active");
        dashboardSidebar.classList.toggle("active");
    });
});
