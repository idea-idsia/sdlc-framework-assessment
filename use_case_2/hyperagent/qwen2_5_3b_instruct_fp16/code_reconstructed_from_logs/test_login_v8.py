def perform_tests():
    # Define test cases as dictionaries for easy iteration and attribute assignment
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

    # Iterate through each test case and simulate form submission
    for test_case in test_cases:
        username = test_case["username"]
        password = test_case["password"]
        userType = test_case["userType"]

        # Create a simple mock form (using dictionary keys as attributes)
        form = {
            "username": "",
            "password": "",
            "userType": ""
        }

        for key, value in test_case.items():
            setattr(form, key.replace("_", "-"), value)

        submit_button = form["submit"]

        # Simulate button click (for demonstration purposes only)
        # In real-world scenario, this would be handled by the user clicking the button
        submit_button.click()

        # Check if the error class is present on the button (indicating validation failure)
        if "error" in str(submit_button):
            print(f"Test failed for input: {test_case}")
            return False

    # All tests passed!
    print("All tests passed!")


perform_tests()