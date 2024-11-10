// Wait for the DOM content to be fully loaded before executing the script
document.addEventListener("DOMContentLoaded", () => {

    // Select all content sections and timeline dots
    const sections = document.querySelectorAll(".content-section");
    const dots = document.querySelectorAll(".timeline-dot");

    // Add an event listener to detect scroll within the content wrapper
    document.querySelector(".content-wrapper").addEventListener("scroll", () => {
        
        // Loop through each section to determine which one is currently in view
        sections.forEach((section, index) => {
            const rect = section.getBoundingClientRect();  // Get the position of each section
            
            // Check if the section is within the viewport
            if (rect.top >= 0 && rect.top < window.innerHeight) {
                // Remove the 'active' class from all dots, then add it to the current dot
                dots.forEach(dot => dot.classList.remove("active"));
                dots[index].classList.add("active");  // Activate the dot that corresponds to the current section
            }
        });
    });

    // Add click event listeners to each timeline item
    document.querySelectorAll('.timeline-item').forEach(item => {
        item.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');  // Get the target section ID from data-target attribute
            const targetSection = document.querySelector(targetId);  // Select the section with the corresponding ID
            
            // Scroll smoothly to the target section when a timeline item is clicked
            targetSection.scrollIntoView({ behavior: 'smooth' });
        });
    });
});

