let contactCount = 1;

function openSidePanel() {
    document.getElementById("sidePanel").style.width = "250px";
}

function closeSidePanel() {
    document.getElementById("sidePanel").style.width = "0";
}

function logout() {
    alert('Logged out successfully!');
    window.location.href = 'index.html';
}

// Save contact to backend
function saveContact(phoneNumber) {
    fetch('/save_contact', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone_number: phoneNumber })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message || data.error);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    const phoneForm = document.getElementById('phoneForm');
    const phoneInput = document.getElementById('phone');
    const errorText = document.getElementById('error');

    phoneForm.addEventListener('submit', function(event) {
        const phoneValue = phoneInput.value.trim();

        // Check: only digits, exactly 10 digits
        const isValid = /^\d{10}$/.test(phoneValue);

        if (!isValid) {
            errorText.textContent = "Please enter a valid 10-digit phone number with digits only.";
            event.preventDefault(); // Prevent form submission
        } else {
            errorText.textContent = ""; // Clear error if valid
            event.preventDefault(); // Prevent default form submission
            saveContact(phoneValue);
        }
    });
});