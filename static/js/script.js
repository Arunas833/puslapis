// Patikrina, ar JavaScript failas sėkmingai įkeltas
console.log("JavaScript sėkmingai užkrautas!");

// Fiksuotas meniu keičiasi scrolinant
window.addEventListener("scroll", function() {
    let nav = document.querySelector("nav");
    if (window.scrollY > 50) {
        nav.style.background = "#002244"; // Tamsesnė spalva scrolinant
    } else {
        nav.style.background = "rgba(0, 51, 102, 0.9)";
    }
});

// Pridėk aktyvios nuorodos efektą navigacijoje
document.querySelectorAll("nav ul li a").forEach(link => {
    link.addEventListener("click", function() {
        document.querySelectorAll("nav ul li a").forEach(el => el.classList.remove("active"));
        this.classList.add("active");
    });
});
