def perform_tests():
    # Test cases for username validation (invalid)
    invalid_username_cases = [
        {"username": "", "password": "pass123", "userType": "simple-user"},
        {"username": "test_user", "password": "wrong_pass", "userType": "helpdesk-staff"}
    ]

    # Test cases for password validation (invalid)
    invalid_password_cases = [
        {"username": "", "password": "pass123", "userType": "simple-user"},
        {"username": "test_user", "password": "wrong_pass", "userType": "helpdesk-staff"}
    ]

    # Test case with empty fields
    no_fields_case = {
        "username": "",
        "password": "",
        "userType": ""
    }

    for test_case in invalid_username_cases:
        form = document.loginForm
        form.username.value = test_case["username"]
        form.password.value = test_case["password"]
        form.userType.value = test_case["userType"]

        submit_button = form.querySelector("button")
        if not submit_button.classList.contains('error'):
            result_element = form.querySelector('#generalError')
            if result_element:
                print(f"Test failed for input: {test_case}")
                return False

    # Test case with empty password
    for test_case in invalid_password_cases:
        form = document.loginForm
        form.username.value = test_case["username"]
        form.password.value = "wrong_pass"
        form.userType.value = test_case["userType"]

        submit_button = form.querySelector("button")
        if not submit_button.classList.contains('error'):
            result_element = form.querySelector('#generalError')
            if result_element:
                print(f"Test failed for input: {test_case}")
                return False

    # Test case with empty fields
    form = document.loginForm
    form.username.value = ""
    form.password.value = ""
    form.userType.value = ""

    submit_button = form.querySelector("button")
    if not submit_button.classList.contains('error'):
        result_element = form.querySelector('#generalError')
        if result_element:
            print(f"Test failed for input: {no_fields_case}")
            return False

    # All tests passed!
    print("All tests passed!")


perform_tests()