document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Validate username (required and alphanumeric)
    var username = document.getElementById('username');
    if (!/^[a-zA-Z0-9]+$/.test(username.value)) {
        username.classList.add('error');
        document.getElementById('usernameError').innerText = "Username must contain only letters and numbers.";
        return false;
    } else {
        username.classList.remove('error');
    }

    // Validate password (minimum 8 characters, at least one uppercase, one lowercase, and one digit)
    var password = document.getElementById('password');
    if (!/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(password.value)) {
        password.classList.add('error');
        document.getElementById('passwordError').innerText = "Password must be at least 8 characters with one uppercase letter, one lowercase letter, and one digit.";
        return false;
    } else {
        password.classList.remove('error');
    }

    // Validate user type (required)
    var userType = document.getElementById('userType');
    if (!userType.value) {
        userType.classList.add('error');
        document.getElementById('userTypeError').innerText = "User Type is required.";
        return false;
    } else {
        userType.classList.remove('error');
    }

    // If all validations pass, proceed with form submission
    alert("Form submitted successfully!");
});