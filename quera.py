import os
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_quera():
    driver = webdriver.Chrome()
    driver.get("https://www.quera.org")

    # Login
    signin_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/header/header/div/div[5]/div/div/a[2]'))
    )
    signin_button.click()

    email = os.environ.get('QUERA_EMAIL')
    password = os.environ.get('QUERA_PASSWORD')

    if not email:
        email = input('Enter your quera email: ')
    if not password:
        password = getpass('Enter your quera password: ')

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/div[1]/div/input'))
    )
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password-input"]'))
    )
    password_input.send_keys(password)

    signin_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-container"]/div[3]/form/div[4]/button'))
    )
    signin_submit_button.click()

    return driver

def create_new_class(driver):
    developer_course_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="qnav__rightmenu"]/a[1]'))
    )
    developer_course_button.click()

    add_course_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="body_container"]/div[1]/div/div[1]/div[1]/div[2]/a[1]'))
    )
    add_course_button.click()
    
    name = 'شهید بهشتی'
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="body_container"]/div/div[2]/div[1]/form/div[1]/div/div/input[2]'))
    )
    name_input.send_keys(name)

    time.sleep(4)
    choose_name_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="school_menu"]/div[1]/span'))
    )
    choose_name_button.click()
    time.sleep(4)

    class_name = 'my class'
    class_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id_course'))
    )
    class_name_input.send_keys(class_name)

    time.sleep(4)

    phone = os.environ.get('PHONE')
    if not phone:
        phone = input("Enter your phone number")

    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'id_phone_number'))
    )
    phone_input.send_keys(phone)
    time.sleep(4)

    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="body_container"]/div/div[2]/div[1]/form/div[3]/div[2]/div/div[1]'))
    )
    dropdown.click()

    choose_semester_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="body_container"]/div/div[2]/div[1]/form/div[3]/div[2]/div/input'))
    )
    choose_semester_button.click()
    time.sleep(4)

    submit_semester_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="body_container"]/div/div[2]/div[1]/form/div[3]/div[2]/div/div[2]/div[1]'))
    )
    submit_semester_button.click()


    create_class_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="body_container"]/div/div[2]/div[1]/form/button'))
    )
    create_class_button.click()

    time.sleep(14)


driver = login_to_quera()
create_new_class(driver)