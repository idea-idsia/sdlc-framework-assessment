def perform_tests():
    # Test case 1: Empty username, correct password, userType.
    test_case = {
        "username": "",
        "password": "pass123",
        "userType": "simple-user"
    }

    form = document.loginForm
    for key, value in test_case.items():
        setattr(form, key.replace("_", "-"), value)

    submit_button = form.querySelector("button")
    if not submit_button.classList.contains('error'):
        print(f"Test failed for input: {test_case}")
        return False

    # Test case 2: Valid username, incorrect password, userType.
    test_case = {
        "username": "test_user",
        "password": "wrong_pass",
        "userType": "helpdesk-staff"
    }

    form = document.loginForm
    for key, value in test_case.items():
        setattr(form, key.replace("_", "-"), value)

    submit_button = form.querySelector("button")
    if not submit_button.classList.contains('error'):
        print(f"Test failed for input: {test_case}")
        return False

    # Test case 3: Invalid username, valid password, empty userType.
    test_case = {
        "username": "invalid_user",
        "password": "correct_pass",
        "userType": ""
    }

    form = document.loginForm
    for key, value in test_case.items():
        setattr(form, key.replace("_", "-"), value)

    submit_button = form.querySelector("button")
    if not submit_button.classList.contains('error'):
        print(f"Test failed for input: {test_case}")
        return False

    # All tests passed!
    print("All tests passed!")


perform_tests()