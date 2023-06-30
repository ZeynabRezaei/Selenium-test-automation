import os
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_abrarvan():
    driver = webdriver.Chrome()
    driver.get("https://accounts.arvancloud.ir/login?lang=fa")

    email = os.environ.get('ARVAN_EMAIL')
    password = os.environ.get('ARVAN_PASSWORD')

    if not email:
        email = input('Enter your email: ')
    if not password:
        password = getpass('Enter your password: ')

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div.l-withBanner__row > div.l-withBanner__content > div > div:nth-child(1) > div > form > div.relative.v1\:ar-textField.p-login__input.p-login__input--email > input'))
    )
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div/div[1]/div/form/div[2]/div/input'))
    )
    password_input.send_keys(password)

    signin_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'login-submit'))
    )
    signin_submit_button.click()
    time.sleep(5)

    return driver

driver = login_to_abrarvan()