import os
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium webdriver
driver = webdriver.Chrome()  # You may need to download and specify the path to your Chrome webdriver here
driver.get("https://torob.ir")

# Check if environment variables are available for login
torob_username = os.getenv("TOROB_USERNAME")
torob_password = os.getenv("TOROB_PASSWORD")

# Function to log in using environment variables
def login_with_envs(username, password):
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".login-button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

# Function to log in with user inputs
def login_with_user_input():
    username = input("Enter your Torob.ir username: ")
    password = getpass("Enter your Torob.ir password: ")

    login_with_envs(username, password)

# Check if environment variables are available for login
if torob_username and torob_password:
    login_with_envs(torob_username, torob_password)
else:
    login_with_user_input()

# Wait for the user to complete any manual verification steps if required
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-field")))

# Search for a product
search_query = input("Enter the product you want to search for: ")
search_field = driver.find_element(By.CSS_SELECTOR, ".search-field")
search_field.send_keys(search_query)
search_field.send_keys(Keys.ENTER)

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results")))

# Purchase the first item in the search results
first_item = driver.find_element(By.CSS_SELECTOR, ".search-results .item")
first_item.click()

# Wait for the item page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".item-page")))

# Perform the purchase action here, e.g., add to cart, proceed to checkout, etc.
# Note: The exact steps depend on the website's layout and functionality.

# Close the browser window
driver.quit()
