from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://terraria.fandom.com/wiki/Weapons')          #Access the website
search = driver.find_element('wds-button wds-is-secondary wiki-tools__search')                  #Find an element
search.click()
search.send_keys('moon')                                        #Type on the field
search.send_keys(Keys.RETURN)
