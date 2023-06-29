import os
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_amazon():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com")

    # Login
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nav-link-accountList'))
    )
    signin_button.click()

    email = os.environ.get('AMAZON_EMAIL')
    password = os.environ.get('AMAZON_PASSWORD')

    if not email:
        email = input('Enter your email: ')
    if not password:
        password = getpass('Enter your password: ')

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ap_email'))
    )
    email_input.send_keys(email)

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'continue'))
    )
    continue_button.click()

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ap_password'))
    )
    password_input.send_keys(password)

    signin_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'signInSubmit'))
    )
    signin_submit_button.click()

    return driver

def purchase_item(driver):
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))
    )
    search_input.clear()

    item_name = input('Enter the item name: ')
    search_input.send_keys(item_name)

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="Go"]'))
    )
    search_button.click()

    # Wait for search results to load properly
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-index="0"]//h2/a'))
    )

    # Get the first item from search results
    first_item = driver.find_element(By.XPATH, '//div[@data-index="0"]//h2/a')
    first_item.click()

    # TODO: Perform the purchase process

    print("Item purchased successfully.")


driver = login_to_amazon()
purchase_item(driver)

time.sleep(4)
driver.quit()
