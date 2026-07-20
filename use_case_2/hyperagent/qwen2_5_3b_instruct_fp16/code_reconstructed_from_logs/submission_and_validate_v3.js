document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Validate username (required and alphanumeric)
    var username = document.getElementById('username');
    if (!/^\w+$/.test(username.value)) {
        username.classList.add('error');
        usernameError.innerHTML = 'Username must be alphanumeric';
        return;
    }
    username.classList.remove('error');

    // Validate password (required, minimum 8 characters, and alphanumeric)
    var password = document.getElementById('password');
    if (!/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(password.value)) {
        password.classList.add('error');
        passwordError.innerHTML = 'Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, and one digit';
        return;
    }
    password.classList.remove('error');

    // Validate user type (required)
    var userType = document.getElementById('userType');
    if (!userType.value) {
        userType.classList.add('error');
        userTypeError.innerHTML = 'User type is required';
        return;
    }
    userType.classList.remove('error');

    // Submit the form if all validations are successful
    document.loginForm.submit();
});