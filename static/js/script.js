document.addEventListener("DOMContentLoaded", () => {

    const sections = document.querySelectorAll(".content-section");
    const dots = document.querySelectorAll(".timeline-dot");

    // Highlight the active dot when scrolling
    document.querySelector(".content-wrapper").addEventListener("scroll", () => {
        sections.forEach((section, index) => {
            const rect = section.getBoundingClientRect();
            if (rect.top >= 0 && rect.top < window.innerHeight) {
                dots.forEach(dot => dot.classList.remove("active"));
                dots[index].classList.add("active");
            }
        });
    });

    // Smooth scroll to section when clicking a timeline item
    document.querySelectorAll('.timeline-item').forEach(item => {
        item.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetSection = document.querySelector(targetId);
            targetSection.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Handle question button clicks
    document.querySelectorAll('.question-btn').forEach(button => {
        button.addEventListener('click', () => {
            // Clear any previous feedback
            button.parentNode.querySelectorAll('.question-btn').forEach(btn => {
                btn.classList.remove('correct', 'incorrect');
            });

            // Check if the clicked button is correct
            if (button.getAttribute('data-correct') === 'true' | button.getAttribute('data-correct') === 'True') {
                button.classList.add('correct'); // Mark as correct
                alert("Correct!");
            } else {
                button.classList.add('incorrect'); // Mark as incorrect
                alert("Incorrect! Try again.");
            }
        });
    });
});