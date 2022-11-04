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
1. Enter your correct login credentials as specified at lines 21, 22, 87, 88, 96, 97, 112, 142
2. Run the tests with:
> pytest test.py
