import os
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_snapp():
    driver = webdriver.Chrome()
    driver.get("https://snapp.ir")

    time.sleep(10)
    login_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/main/section[1]/div[1]/div[3]/a/button'))
    )
    login_button.click()

    phone = os.environ.get('PHONE')
    if not phone:
        phone = input('Enter your phone number: ')

    phone_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/div/form/main/div/div/div[1]/input'))
    )
    phone_input.send_keys(phone)

    next_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/main/div[4]/div/form/div/button'))
    )
    next_button.click()

    verification_code = input('Enter your verification code: ')
    verification_code_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/main/div[4]/div/main/div[4]/div/div[1]/input'))
    )
    verification_code_input.send_keys(verification_code)
    time.sleep(10)
    # Check if exit button exists and click it if it does
    # /html/body/div[3]/div/div[1]/div[1]/button/span[1]/svg/path
    # body > div:nth-child(5) > div > div.css-1lyybie > div.css-1lyb01m > button > span.css-94qwli > svg > path
    # document.querySelector("body > div:nth-child(5) > div > div.css-1lyybie > div.css-1lyb01m > button > span.css-94qwli > svg > path")
    exit_button = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/div[1]/button/span[1]/svg')
    #/html/body/div[3]/div/div[1]/div[2]/div[2]/div/button[1]
    # <button color="neutral" class="css-2k6mk7" style="position: relative;"><span class="css-94qwli">انصراف</span><span class="css-19a09oi"></span></button>
    # body > div:nth-child(5) > div > div.css-1lyybie > div.css-fepz1c > div.css-1kdcb46 > div > button.css-2k6mk7
    # document.querySelector("body > div:nth-child(5) > div > div.css-1lyybie > div.css-fepz1c > div.css-1kdcb46 > div > button.css-2k6mk7")
    # /html/body/div[3]/div/div[1]/div[2]/div[2]/div/button[1]
    enseraf_button = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div[2]/div/button[1]')
    #<button color="primary" class="css-1mwng2t" style="position: relative;"><span class="css-94qwli">فعال‌سازی</span><span class="css-19a09oi"></span></button>
    # body > div:nth-child(5) > div > div.css-1lyybie > div.css-fepz1c > div.css-1kdcb46 > div > button.css-1mwng2t
    # document.querySelector("body > div:nth-child(5) > div > div.css-1lyybie > div.css-fepz1c > div.css-1kdcb46 > div > button.css-1mwng2t")
    # /html/body/div[3]/div/div[1]/div[2]/div[2]/div/button[2]
    okay_button = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[1]/div[2]/div[2]/div/button[2]') 
    if exit_button:
        exit_button[0].click()
        print("exit button clicked")
    elif enseraf_button: 
        enseraf_button[0].click()
        print("enseraf button clicked")
    elif okay_button:
        okay_button[0].click()
        print("okay button clicked")
    else:
        print("buttons not found")            

    return driver


def get_ride(driver):
   
    ride_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/main/div[4]/footer/div/div/div[2]/div/div/div[1]/div/div/div/div/img'))
    )
    ride_button.click()

    begin_loc = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/button/div[1]/div[1]'))
    )
    begin_loc.click()

    search_dest = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/main/div[4]/footer/div[2]/div[1]/div[2]/div/h6'))
    )
    search_dest.click()

    dest = "دانشگاه شهید بهشتی"

    if not dest: 
        dest = input('Enter your destination: ')

    type_dest = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[19]/div/div[1]/div/div/main/form/div/div/div[1]/input'))
    )
    type_dest.click()

    choose_dest = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[21]/div/div[1]/div/div/main/div[2]/ul/li[1]/div/div/div[1]/div[2]/p[2]'))
    )
    choose_dest.click()

    dest_loc = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/main/div[4]/div[1]/div[2]/div/div[2]/div[1]/button/div[1]/div[1]/div'))
    )
    dest_loc.click()
    
    request_for_ride = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/main/div/main/div[4]/footer/div[3]/div/button/span[1]'))
    )
    request_for_ride.click()
   

driver = login_to_snapp()
get_ride(driver)

time.sleep(4)
driver.quit()

