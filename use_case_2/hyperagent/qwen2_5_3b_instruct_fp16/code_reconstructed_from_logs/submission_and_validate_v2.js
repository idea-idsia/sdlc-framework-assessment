document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Validate username (required)
    var username = document.getElementById('username');
    if (!/^\w+$/.test(username.value)) {
        username.classList.add('error');
        usernameError.innerHTML = 'Username must be alphanumeric';
        return;
    }
    username.classList.remove('error');

    // Validate password (required and minimum 8 characters)
    var password = document.getElementById('password');
    if (password.value.length < 8) {
        password.classList.add('error');
        passwordError.innerHTML = 'Password must be at least 8 characters long';
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