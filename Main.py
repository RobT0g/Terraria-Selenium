import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://terraria.fandom.com/wiki/Weapons')              #Access the website
search = driver.find_element(By.CLASS_NAME, "mw-parser-output")     #Find an element
search.send_keys

time.sleep(5)
