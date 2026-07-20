# Placeholder for testing function
def perform_tests():
    form = document.loginForm

    # Test case 1: Empty username, correct password, userType.
    form.username.value = ""
    form.password.value = "pass123"
    form.userType.value = "simple-user"

    submit_button = form.querySelector("button")
    if not submit_button.classList.contains('error'):
        result_element = form.querySelector('#generalError')
        if result_element:
            print(f"Test failed for input: {form.username.value}, {form.password.value}, {form.userType.value}")
            return False

    # Test case 2: Valid username, incorrect password, userType.
    form.username.value = "test_user"
    form.password.value = "wrong_pass"
    form.userType.value = "helpdesk-staff"

    submit_button = form.querySelector("button")
    if not submit_button.classList.contains('error'):
        result_element = form.querySelector('#generalError')
        if result_element:
            print(f"Test failed for input: {form.username.value}, {form.password.value}, {form.userType.value}")
            return False

    # Test case 3: Invalid username, valid password, empty userType.
    form.username.value = "invalid_user"
    form.password.value = "correct_pass"
    form.userType.value = ""

    submit_button = form.querySelector("button")
    if not submit_button.classList.contains('error'):
        result_element = form.querySelector('#generalError')
        if result_element:
            print(f"Test failed for input: {form.username.value}, {form.password.value}, {form.userType.value}")
            return False

    # All tests passed!
    print("All tests passed!")


perform_tests()