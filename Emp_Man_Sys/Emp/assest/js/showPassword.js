function validateForm(event) {
    event.preventDefault();
    const passwordInput = document.getElementById("password").value;
    const cpasswordInput = document.getElementById("cpassword").value;
    const mismatchSpan = document.getElementById("password-mismatch");
    console.log("passwordInput:", passwordInput);
    console.log("cpasswordInput:", cpasswordInput);
    if (passwordInput !== cpasswordInput) {
        mismatchSpan.textContent = "Passwords do not match!";
        // Prevent form submission
    } else {
        mismatchSpan.textContent = "";
        document.querySelector('form').submit();
         // Allow form submission
    }
}

function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const toggleIcon = document.querySelector(".toggle-password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.innerHTML = "&#128065;"; // Show the open-eye icon
    } else {
        passwordInput.type = "password";
        toggleIcon.innerHTML = "&#128064;"; // Show the closed-eye icon
    }
}

function toggleCPasswordVisibility() {
    const cpasswordInput = document.getElementById("cpassword");
    const ctoggleIcon = document.querySelector(".toggle-cpassword");

    if (cpasswordInput.type === "password") {
        cpasswordInput.type = "text";
        ctoggleIcon.innerHTML = "&#128065;"; // Show the open-eye icon
    } else {
        cpasswordInput.type = "password";
        ctoggleIcon.innerHTML = "&#128064;"; // Show the closed-eye icon
    }
}

