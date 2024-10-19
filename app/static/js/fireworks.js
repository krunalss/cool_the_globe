// Track the user's progress
let completedActions = 0;

function showBrowniePoints(element) {
    // If all actions have already been completed, show the congratulations popup
    if (completedActions >= 5) {
        showCongratulationsPopup();
        return;
    }

    // Check if the action has already been completed
    if (element.dataset.completed === "true") {
        return; // Skip if already completed
    }

    // Mark the action as completed
    element.dataset.completed = "true";

    // Increase completed actions count
    completedActions++;

    // Display progress pop-up message
    const progressPopup = document.getElementById('progress-popup');
    const progressText = document.getElementById('progress-popup-text');

    if (progressPopup && progressText) {
        if (completedActions < 5) {
            progressText.innerHTML = `Step ${completedActions} of 5 completed!`;
            progressPopup.style.display = 'block';
        } else {
            // If all actions are completed, show the congratulations pop-up
            showCongratulationsPopup();
        }
    }
}

function closePopup() {
    const popup = document.getElementById('progress-popup');
    if (popup) {
        popup.style.display = 'none';
    }
}

function showCongratulationsPopup() {
    const congratulationsPopup = document.getElementById('congratulations-popup');
    if (congratulationsPopup) {
        congratulationsPopup.style.display = 'block';
    }
}

function closeCongratulationsPopup() {
    const popup = document.getElementById('congratulations-popup');
    if (popup) {
        popup.style.display = 'none';
    }
}

// Close progress pop-up if user clicks anywhere outside the pop-up content
window.onclick = function (event) {
    const progressPopup = document.getElementById('progress-popup');
    if (event.target === progressPopup) {
        progressPopup.style.display = 'none';
    }

    const congratulationsPopup = document.getElementById('congratulations-popup');
    if (event.target === congratulationsPopup) {
        congratulationsPopup.style.display = 'none';
    }
}
