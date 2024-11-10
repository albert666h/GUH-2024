window.addEventListener('scroll', function() {
    const yearSections = document.querySelectorAll('.year');
    const scrollPosition = window.scrollY + window.innerHeight / 2; // Middle of viewport

    yearSections.forEach(section => {
        const rect = section.getBoundingClientRect();
        
        // Check if the section is in the middle of the viewport
        if (rect.top <= window.innerHeight / 2 && rect.bottom >= window.innerHeight / 2) {
            section.classList.add("active");

            // Retrieve the color associated with this section and lighten it for the gradient
            const baseColor = section.getAttribute('data-bottom-color');
            
            // Create a vertical gradient from a light version of the color to the base color
            const gradient = `linear-gradient(180deg, ${lightenColor(baseColor, 0.7)}, ${baseColor})`;
            
            // Apply the gradient color as the background of the body
            document.body.style.background = gradient;

        } else {
            section.classList.remove("active");
        }
    });
});

// Helper function to lighten a hex color
function lightenColor(hex, amount) {
    const num = parseInt(hex.replace("#", ""), 16);
    const r = Math.min(255, (num >> 16) + 255 * amount);
    const g = Math.min(255, ((num >> 8) & 0x00FF) + 255 * amount);
    const b = Math.min(255, (num & 0x0000FF) + 255 * amount);
    return `rgb(${r}, ${g}, ${b})`;
}




// // JavaScript to change the background color on scroll
// window.addEventListener('scroll', function() {
//     const yearSections = document.querySelectorAll('.year');
//     const scrollPosition = window.scrollY + window.innerHeight / 2; // Detect middle of the page

//     yearSections.forEach(section => {
//         const rect = section.getBoundingClientRect();
        
//         // If the section is in the viewport (adjust as needed)
//         if (rect.top <= scrollPosition && rect.bottom >= scrollPosition) {
//             const year = section.getAttribute('data-year');
            
//             // Set background color based on the year or any other condition
//             switch(year) {
//                 case "2021":
//                     document.body.style.background = "linear-gradient(180deg, #0c3357, #9AFD7F)";
//                     break;
//                 case "2022":
//                     document.body.style.background = "linear-gradient(180deg, #4B8B8C, #1D3C3C)";
//                     break;
//                 case "2023":
//                     document.body.style.background = "linear-gradient(180deg, #6C8B3D, #3E5B4C)";
//                     break;
//                 // Add more cases for additional years or conditions
//             }
//         }
//     });
// });


