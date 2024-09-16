# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# importing webdriver and manager to install webdriver automatically
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(3)

# target link to visit
demo_link="https://www.saucedemo.com/"
driver.get(demo_link)
time.sleep(3)

# entering username 
driver.find_element(By.NAME, "user-name").send_keys("standard_user" )
time.sleep(5)

# entering password
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
time.sleep(5)

# clicking login button
driver.find_element(By.NAME, "login-button").click()
time.sleep(5)

# get title of the web page
web_page_title = driver.title
print(web_page_title)

# get url
web_page_url = driver.current_url
print(web_page_url)

# get contents of the web page
page_content = driver.find_element(By.TAG_NAME, 'body').text

with open("Webpage_task_11.txt", mode="w") as f:
    f.write(page_content)

# Print the page content
print(page_content)