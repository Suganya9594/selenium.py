from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# open the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
# Open the URL
#driver.get(" https://demoqa.com/droppable")
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)

# source and target element (draggable and droppable)
# driver.switch_to.frame(0) -  this is one type of working method
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, 'demo-frame')) #this is another type of working method
source_element = driver.find_element(By.XPATH, '//*[@id="draggable"]')
target_element = driver.find_element(By.XPATH, '//*[@id="droppable"]')
time.sleep(3)

# Create an ActionChains object
actions = ActionChains(driver)
time.sleep(2)


actions.drag_and_drop(source_element,target_element).perform()
time.sleep(3)

#close the driver
driver.quit











