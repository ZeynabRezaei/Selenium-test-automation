import os
import time
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_virgool(email, password):
    # Set up the web driver (in this example, we'll use Chrome)
    driver = webdriver.Chrome()

    # Navigate to Virgool.io
    driver.get('https://virgool.io')

    # Wait for the sign-in button to be clickable
    sign_in_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="btn-text" and @href="https://virgool.io/login" and @title="ورود به حساب کاربری"]'))
    )

    # Click the sign-in button
    sign_in_button.click()

    # Find the email input field and enter the login email
    email_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="userInput"]'))
    )
    email_input.send_keys(email)

    # Find the "Next" button and click it
    next_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(.,"ورود به حساب کاربری")]'))
    )
    next_button.click()

    # Find the password input field and enter the password
    password_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
    )
    password_input.send_keys(password)

    # Find the sign-in button and click it
    sign_in_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(.,"ورود به حساب کاربری")]'))
    )
    sign_in_button.click()

    # Wait for the login process to complete
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/@")]'))
        )
        print('Login successful!')
    except:
        print('Login failed.')
        driver.quit()  # Quit the driver if login fails
        return None

    # Return the driver instance
    return driver

def create_new_post(driver, title, text):
    # Find the new post button and click it
    new_post_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/section/header/section/section/div[2]/section/div[1]/div/a'))
    )
    new_post_button.click()

    print('Creating a new post...')

    #input title
    title_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-app"]/section/div[1]/div[1]/input'))
    )
    title_input.send_keys(title)

    #input text
    text_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-app"]/section/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div'))
    )
    text_input.send_keys(text)

    # simple text to use as an input: 
    # The quick brown fox jumps over the lazy dog.
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    # Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. 
    # Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit. 
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    
    publish_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-publish"]'))
    )
    publish_button.click()

    time.sleep(2)

    exit_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="react-app"]/section/div[2]/div/div'))
    )
    exit_button.click()

    time.sleep(2)

def home(driver):
    home_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > section > header > section > section > div.container > section > div:nth-child(1) > a > svg'))
    )

    # Click the home button
    home_button.click()
    print("Successfully back to home")
    time.sleep(5)



# Retrieve the email & password from the environment variable
virgool_email = os.environ.get('VIRGOOL_EMAIL')
virgool_password = os.environ.get('VIRGOOL_PASSWORD')

title = os.environ.get('VIRGOOL_TITLE')
text = os.environ.get('VIRGOOL_TEXT')

# If the environment variable is not set, prompt the user to enter the email & password
if not virgool_email:
    virgool_email = input('Enter your Virgool.io email: ')

if not virgool_password:
    virgool_password = getpass('Enter your Virgool.io password: ')  
#mr4^2WZ7I1GDi8
if not title:
    title = input('Enter a title: ')

if not text:
    text = input('Enter your text: ') 

# Login to Virgool.io
driver = login_to_virgool(virgool_email, virgool_password)

# Check if login was successful before proceeding
if driver is not None:
    # Call the create_new_post method
    create_new_post(driver, title, text)

if driver is not None:
    home(driver)

# Close the browser
driver.quit()
