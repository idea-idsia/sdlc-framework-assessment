# Placeholder for testing function
def perform_tests():
    test_cases = [
        {
            "username": "",
            "password": "pass123",
            "userType": "simple-user"
        },
        {
            "username": "test_user",
            "password": "wrong_pass",
            "userType": "helpdesk-staff"
        },
        {
            "username": "invalid_user",
            "password": "correct_pass",
            "userType": ""
        }
    ]

    for test_case in test_cases:
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

    print("All tests passed!")


perform_tests()