from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

correct_user = "enter correct email here"
correct_pass = "enter correct password here"

# setUp
url = "http://www.hudl.com/login"
chromepath = r"C:\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chromepath))
driver.maximize_window()


def reset():
    driver.get(url)
    time.sleep(3)


def test_login():  # successful login
    reset()
    user = correct_user
    passw = correct_pass
    username = driver.find_element("name", "email")
    username.clear()
    username.send_keys(user)
    password = driver.find_element("name", "password")
    password.clear()
    password.send_keys(passw)
    driver.find_element("id", "logIn").click()
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/home'


def test_login_wrong_username_and_password():  # wrong username and password
    reset()
    user = "wrong@gmail.com"
    passw = "wrongpassword"
    username = driver.find_element("name", "email")
    username.clear()
    username.send_keys(user)
    password = driver.find_element("name", "password")
    password.clear()
    password.send_keys(passw)
    driver.find_element("id", "logIn").click()
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "uni-text").text
    assert result == "We didn't recognize that email and/or password.Need help?"


def test_sign_up():  # sign up
    reset()
    driver.find_element(By.CLASS_NAME, 'uni-link.uni-link--default.styles_signUpLink_1CPc8TbK9yDyBdJiSpUOZV').click()
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/register/signup'


def test_login_with_organization():  # login with an organization
    reset()
    driver.find_element(By.CLASS_NAME, 'uni-button.uni-button--wrap.uni-button--minimal').click()
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/app/auth/login/organization'


def test_need_help():  # need help
    reset()
    driver.find_element(By.XPATH, "//*[@data-qa-id = 'need-help-link']").click()
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/login/help#'


def test_back():  # back arrow at top left
    reset()
    driver.find_element(By.CLASS_NAME, 'styles_backIcon_1nBYGKhbTIbTmIULDJg1MZ').click()
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/home'


def test_hudl_logo():  # Hudl logo
    reset()
    driver.find_element(By.CLASS_NAME, 'uni-link.uni-link--wrapper').click()
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/home'


def test_login_using_keys():  # login with tab and enter
    reset()
    user = correct_user
    passw = correct_pass
    driver.find_element("name", "email").send_keys(user + Keys.TAB + passw + Keys.ENTER)
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/home'


def test_login_remember_me():  # login with remember me
    reset()
    user = correct_user
    passw = correct_pass
    username = driver.find_element("name", "email")
    username.clear()
    username.send_keys(user)
    password = driver.find_element("name", "password")
    password.clear()
    password.send_keys(passw)
    driver.find_element(By.CLASS_NAME, 'uni-form__check-item').click()
    driver.find_element("id", "logIn").click()
    time.sleep(3)
    assert driver.current_url == 'https://www.hudl.com/home'


def test_login_wrong_password():  # wrong password
    reset()
    user = correct_user
    passw = "wrongpassword"
    username = driver.find_element("name", "email")
    username.clear()
    username.send_keys(user)
    password = driver.find_element("name", "password")
    password.clear()
    password.send_keys(passw)
    driver.find_element("id", "logIn").click()
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "uni-text").text
    assert result == "We didn't recognize that email and/or password.Need help?"


def test_login_no_username():  # no username
    reset()
    passw = "wrongpassword"
    username = driver.find_element("name", "email")
    username.clear()
    password = driver.find_element("name", "password")
    password.clear()
    password.send_keys(passw)
    driver.find_element("id", "logIn").click()
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "uni-text").text
    assert result == "We didn't recognize that email and/or password.Need help?"


def test_login_no_password():  # no password
    reset()
    user = correct_user
    username = driver.find_element("name", "email")
    username.clear()
    username.send_keys(user)
    password = driver.find_element("name", "password")
    password.clear()
    driver.find_element("id", "logIn").click()
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "uni-text").text
    assert result == "We didn't recognize that email and/or password.Need help?"


def test_login_no_username_or_password():  # no username or password
    reset()
    username = driver.find_element("name", "email")
    username.clear()
    password = driver.find_element("name", "password")
    password.clear()
    driver.find_element("id", "logIn").click()
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "uni-text").text
    assert result == "We didn't recognize that email and/or password.Need help?"


def tearDown():
    # close the browser
    driver.quit()
