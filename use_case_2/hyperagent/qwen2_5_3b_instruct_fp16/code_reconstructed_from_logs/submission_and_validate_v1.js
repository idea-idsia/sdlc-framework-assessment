document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var userType = document.getElementById('userType');

    // Validate username (optional, just for demonstration)
    if (!/^\w+$/.test(username.value)) {
        username.classList.add('error');
        usernameError.innerHTML = 'Username must be alphanumeric';
        return;
    }
    username.classList.remove('error');

    // Validate password (optional, just for demonstration)
    if (password.value.length < 8) {
        password.classList.add('error');
        passwordError.innerHTML = 'Password must be at least 8 characters long';
        return;
    }
    password.classList.remove('error');

    // Additional validation for userType
    if (!userType.value) {
        userType.classList.add('error');
        document.getElementById('userTypeError').innerHTML = 'User type is required';
        return;
    }

    userType.classList.remove('error');

    // Submit the form if all validations are successful
    document.loginForm.submit();
});