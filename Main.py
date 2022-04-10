import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://terraria.fandom.com/wiki/Weapons')                                          #Access the website
search = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "infocard.clearfix.terraria.compact")))
texts = []

for k, i in enumerate(search):
    lists = WebDriverWait(i, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "itemlist")))
    items = WebDriverWait(lists, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "i")))
    for j in items:
        print(j.text)
driver.quit()
