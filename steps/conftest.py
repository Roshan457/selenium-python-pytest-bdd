import random
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from pytest_bdd import given, when, then, parsers

values = {
    "Username": "Admin",
    "Password": "admin123",
    "first_name" : "FTest",
    "middle_name" : "MTest",
    "last_name" : "LTest",
    "new_username": "User" + str(random.randint(0,100)),
    "pass": "correct_pass",
    "wrong_pass": "wrong_pass"
}


locators = {
    "Username": (By.NAME, "username"),
    "Password": (By.NAME, "password"),
    "Login Button": (By.XPATH, "//button[@type='submit']"),
    "Dashboard": (By.XPATH, "//h6[text()='Dashboard']"),
    "pim" : (By.XPATH, "//span[contains(.,'PIM')]/parent::a"),
    "add_btn" : (By.XPATH, '//button[normalize-space(.)="Add"]'),
    "create_cred" : (By.XPATH, "//span[@class = 'oxd-switch-input oxd-switch-input--active --label-right']"),
    "first_name" : (By.CSS_SELECTOR, "input[name = 'firstName']"),
    "middle_name" : (By.CSS_SELECTOR, "input[name = 'middleName']"),
    "last_name" : (By.CSS_SELECTOR, "input[name = 'lastName']"),
    "new_username": (By.XPATH, "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input"),
    "pass": (By.XPATH, "//label[text()='Password']/ancestor::div[contains(@class,'oxd-input-group')]//input"),
    "wrong_pass": (By.XPATH,
                   "//label[text()='Confirm Password']/ancestor::div[contains(@class,'oxd-input-group')]//input"),
    "error_message" : (By.XPATH,"//label[text() = 'Confirm Password']//ancestor::div[@class = 'oxd-input-group oxd-input-field-bottom-space']//span")

}

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver

# Find locators
def get_locator(element_name):
    if element_name not in locators:
        raise Exception(
            f"Locator '{element_name}' is not defined."
        )
    return locators[element_name]

# Find inputs
def get_input_values(value):
    if value not in values:
        raise Exception(
            f"Locator '{value}' is not defined."
        )
    return values[value]

@given("User visits the OrangeHRM Application")
def step_impl(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

@when(parsers.parse('User clicks on the "{element}"'))
def step_impl(driver, element):
    locator = get_locator(element)
    element_to_click = driver.find_element(*locator)
    element_to_click.click()
    time.sleep(2)

@when(parsers.parse('User should be able to input "{value}" in "{element}" field'))
def step_impl(driver, value, element):
    locator = get_locator(element)
    values = get_input_values(value)
    field = driver.find_element(*locator)
    field.clear()
    field.send_keys(values)


@then(parsers.parse('Verify the "{element}" is visible'))
def step_impl(driver, element):
    locator = get_locator(element)
    element_to_verify = driver.find_element(*locator)
    assert element_to_verify.is_displayed()

@then(parsers.parse('Verify the "{element}" shows a message "{message}"'))
def step_impl(driver, element, message):
    locator = get_locator(element)
    target_element = driver.find_element(*locator)
    target_element_text = target_element.text
    assert message in target_element_text


