document.addEventListener("scroll", function() {
    const years = document.querySelectorAll(".year");
    const windowHeight = window.innerHeight;

    years.forEach((year) => {
        const rect = year.getBoundingClientRect();
        if (rect.top >= 0 && rect.top <= windowHeight / 2) {
            year.classList.add("active");
        } else {
            year.classList.remove("active");
        }
    });
});




