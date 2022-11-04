# Hudl QA Test

## The Ask
- Setup an automation environment on your local machine using Selenium
- Automate any cases that you would think are good to test the functionality of validating logging into hudl.com.
- Push your tests to a GitHub repository (a public repo is fine) and share the link (please do not include any passwords in a public repo).

## I automated the cases using pytest. The cases I am testing are:
1. Correct username and password
2. Wrong username and password
3. Clicking the "Sign Up" link
4. Clicking the "Log In with an Organization" button
5. Clicking the "Need help?" link
6. Clicking the back arrow to return to home
7. Clicking the Hudl logo to return to home
8. Logging in successfully using tab and enter instead of clicking
9. Logging in successfully with "Remember Me" toggled
10. Wrong password but correct username
11. No username
12. No password
13. No username or password

## To test the program using pytest: 
0. Install Python and Selenium. Make sure the ChromeDriver executable is available in the $PATH variable.
1. Enter your correct login credentials as specified at lines 7 and 8
2. Run the tests with:
> pytest test.py
3. When it finishes running, it will state which tests passed (worked as expected) and which ones failed (did not work as expected).

## Notes
I have attached a zipped screen recording of the code running with pytest.

I developed and ran this program in the following environment:
- Python 3.9.13
- Selenium 4.6.0
- ChromeDriver 107.0.5304.62
