import os
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_sbu():
    driver = webdriver.Chrome()
    driver.get("https://mail.sbu.ac.ir")

    user = os.environ.get('SBU_USER')
    password = os.environ.get('SBU_PASSWORD')

    if not user:
        user = input('Enter your sbu user: ')
    if not password:
        password = getpass('Enter your sbu password: ')

    user_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )
    user_input.send_keys(user)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_input.send_keys(password)

    signin_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lgnDiv"]/div[11]/div/span'))
    )
    signin_submit_button.click()

    return driver

def new_email(driver):

    person = "mh.nasiri"
    person_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, '//*[@id="primaryContainer"]/div[5]/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/form/div/input'))
    )
    person_input.send_keys(person)

    # new_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="primaryContainer"]/div[5]/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/form/div/input'))
    # )
    # new_button.click()
    time.sleep(10)
driver = login_to_sbu()
new_email(driver)