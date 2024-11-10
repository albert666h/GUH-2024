document.addEventListener("scroll", function() {
    const years = document.querySelectorAll(".year");
    const windowHeight = window.innerHeight;  // Height of the visible area of the viewport

    years.forEach((year) => {
        const rect = year.getBoundingClientRect();
        
        // Check if the year section is in the middle of the viewport
        if (rect.top >= 0 && rect.top <= windowHeight / 2) {
            year.classList.add("active");

            // Retrieve the color associated with this year
            const topColor = year.getAttribute('data-year-color'); 
            const bottomColor = year.getAttribute('data-bottom-color'); 
            
            // Generate a vertical gradient from topColor to a transparent light grey to bottomColor
            const gradient = `linear-gradient(180deg, ${bottomColor}, ${bottomColor})`;
            
            // Apply the gradient color as the background of the body
            document.body.style.background = gradient;

        } else {
            year.classList.remove("active");
        }
    });
});
