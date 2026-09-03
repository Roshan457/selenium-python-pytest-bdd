Feature: Login functionality

    Scenario: Successful login

        Given User visits the OrangeHRM Application
        When User should be able to input "Username" in "Username" field
        And User should be able to input "Password" in "Password" field
        And User clicks on the "Login Button"
        And User clicks on the "pim"
        And User clicks on the "add_btn"
        And User should be able to input "first_name" in "first_name" field
        And User should be able to input "middle_name" in "middle_name" field
        And User should be able to input "last_name" in "last_name" field
        And User clicks on the "create_cred"
        And User should be able to input "new_username" in "new_username" field
        And User should be able to input "pass" in "pass" field
        And User should be able to input "wrong_pass" in "wrong_pass" field
        Then Verify the "error_message" is visible
        And Verify the "error_message" shows a message "Passwords do not match"
