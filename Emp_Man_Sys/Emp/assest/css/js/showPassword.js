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
