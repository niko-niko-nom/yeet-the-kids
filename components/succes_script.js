// Function to display the success message
function showSuccessMessage() {
    const successMessage = document.getElementById('success-message');
    successMessage.classList.remove('hidden');
    successMessage.style.opacity = '1';

    setTimeout(() => {
        successMessage.style.opacity = '0';

        setTimeout(() => {
            successMessage.classList.add('hidden');
        }, 500); // Match the CSS transition duration
    }, 3000); // 3 seconds display time
}

window.onload = function () {
    if (window.location.href.includes('success=true')) {
        showSuccessMessage();
    }
};
