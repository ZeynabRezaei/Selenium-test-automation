import os
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_tamin():

    driver = webdriver.Chrome()
    driver.get("https://account.tamin.ir/auth/login")

    # login
    national_id = os.environ.get('NATIONAL_ID')
    password = os.environ.get('TAMIN_PASSWORD')

    if not national_id:
        national_id = input("Enter Your national id: ")

    if not password:
        password = getpass("Enter your Tamin password: ")    

    national_id_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/input[1]'))
    )
    national_id_input.send_keys(national_id)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/input[2]'))
    )
    password_input.send_keys(password)

    signin_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/form/div[3]/button'))
    )
    time.sleep(5)
    signin_submit_button.click()
    time.sleep(10)

    js_path = 'document.querySelector("body > app-root > app-portal-main > app-portal-main-web > div.row.portal-main-container > div:nth-child(2) > div.portal-main-middle-overlay > div")'
    button = driver.execute_script(f'return {js_path}')
    button.click()

def get_records(driver):

    # signin_submit_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-portal-main/app-portal-main-web/div[1]/div[1]/div[5]/button[2]/span'))
    # )
    # signin_submit_button.click()
    
    insured_people_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-portal-main/app-portal-main-web/div[1]/div[2]/div[2]/div/div'))
    )
    insured_people_button.click()

    accordion_head_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'accordion-head'))
    )
    # /html/body/app-root/app-portal-insured/div/div[2]/div[2]/tamin-accordion-group/tamin-accordion[3]/div[1]
    accordion_head_button.click()

    accordion_subitem_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'accordion-subitem'))
    )
    # /html/body/app-root/app-portal-insured/div/div[2]/div[2]/tamin-accordion-group/tamin-accordion[3]/div[2]/div[1]/div
    accordion_subitem_button.click()

    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-history/app-history-list/div/div[2]/button[1]/span'))
    )
    download_button.click()

    time.sleep(10)

def logout_from_tamin():
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/form/div[3]/button'))
    )
    time.sleep(15)
    logout_button.click()
    time.sleep(10)
    
driver = login_to_tamin()
# get_records(driver)
