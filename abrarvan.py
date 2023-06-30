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
    time.sleep(30)

    # //*[@id="aside_menu_cdn_button"]/div[2]/div[1]
    cdn_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'aside_menu_cdn_button'))
    )
    cdn_button.click()

    time.sleep(50)

    # //*[@id="root"]/div/div[11]/div[3]/div/div/div/div[2]
    # //*[@id="root"]/div/div[12]/div[3]/div/div/div/div[2]
    domain_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[12]/div[3]/div/div/div/div[2]'))
    )
    domain_button.click()

    # //*[@id="app"]/div[1]/div/aside/div[2]/ul/li[2]/div[2]/a[4]/span
    dns_records_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/aside/div[2]/ul/li[2]/div[2]/a[4]/span'))
    )
    dns_records_button.click()

# //*[@id="root"]/div/div[11]/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/button/span/span[2]
    new_records_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[11]/div[3]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/button/span/span[2]'))
    )
    new_records_button.click()
    # //*[@id="cdn-select"]/div/div[2]/span
    # //*[@id="root"]/div/div[11]/div[3]/div/div/div[2]/div[1]/div[2]/div[3]/input
    subdomain = os.environ.get('SUBDOMAIN')

    if not subdomain:
        subdomain = input('Enter your subdomain: ')

    subdomain_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[11]/div[3]/div/div/div[2]/div[1]/div[2]/div[3]/input'))
    )
    subdomain_input.send_keys(subdomain)

    ip_address = os.environ.get('IP_ADDRESS')

    if not ip_address:
        ip_address = input('Enter your IP address: ')
        # 46.102.156.91

    ip_addres_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[11]/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/input'))
    )
    ip_addres_input.send_keys(ip_addres)

    # //*[@id="root"]/div/div[11]/div[3]/div/div/div[3]/div[2]/button[2]

    save_records_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[11]/div[3]/div/div/div[3]/div[2]/button[2]'))
    )
    save_records_button.click()

    return driver

driver = login_to_abrarvan()