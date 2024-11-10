// Simulate loading progress
let progress = 0;
const progressBar = document.getElementById('progress');

function updateProgress() {
    progress += 1;
    progressBar.style.width = `${progress}%`;

    // if (progress >= 100) {
    //     setTimeout(() => {
    //         alert('Memory Unlocked!');
    //     }, 500);
    // }
}

const interval = setInterval(() => {
    if (progress < 100) {
        updateProgress();
    } else {
        clearInterval(interval);
    }
}, 50);
