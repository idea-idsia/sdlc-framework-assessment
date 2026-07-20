function validateLogin() {
    // Validate username (required and alphanumeric)
    var username = document.getElementById('username');
    if (!/^[a-zA-Z0-9]+$/.test(username.value)) {
        document.getElementById('usernameError').innerText = "Username must contain only letters and numbers.";
        return false;
    }

    // Validate password (minimum 8 characters, at least one uppercase, one lowercase, and one digit)
    var password = document.getElementById('password');
    if (!/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(password.value)) {
        document.getElementById('passwordError').innerText = "Password must be at least 8 characters with one uppercase letter, one lowercase letter, and one digit.";
        return false;
    }

    // Validate user type
    var userType = document.getElementById('userType');
    if (userType.value === '') {
        document.getElementById('userTypeError').innerText = "User Type is required.";
        return false;
    }

    return true;
}