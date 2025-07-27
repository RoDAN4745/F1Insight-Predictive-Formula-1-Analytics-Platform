document.addEventListener("DOMContentLoaded", () => {
    const scrollTrigger = document.querySelector(".scroll-down");
    const infoSection = document.querySelector(".info-section");

    scrollTrigger.addEventListener("click", () => {
        infoSection.scrollIntoView({ behavior: "smooth" });
    });
});

window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    navbar.style.background = window.scrollY > 100
        ? "rgba(0, 0, 0, 0.85)"
        : "rgba(0, 0, 0, 0.4)";
});

console.log("Homepage loaded. Video running. Ready to scroll!");
console.log("Teams page loaded!");
    