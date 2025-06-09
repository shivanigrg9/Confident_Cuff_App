// script.js
document.addEventListener("DOMContentLoaded", () => {
    const phoneInput = document.getElementById("phone-number");
    const submitButton = document.querySelector(".phone-input button");
    const googleButton = document.querySelector(".google-login");

    // Phone number validation
    submitButton.addEventListener("click", () => {
        const phoneNumber = phoneInput.value.trim();

        if (phoneNumber === "" || phoneNumber.length !== 10 || isNaN(phoneNumber)) {
            alert("Please enter a valid 10-digit phone number.");
        } else {
            alert(`Phone number ${phoneNumber} submitted successfully!`);
        }
    });

    // Simulated Google login
    googleButton.addEventListener("click", () => {
        alert("Redirecting to Google login...");
        // Replace this with actual Google OAuth implementation if needed
    });


});