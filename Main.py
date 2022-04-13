import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def checkPopUp(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_"))).click()
    except:
        pass

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://terraria.fandom.com/wiki/Silver_Shortsword')
driver.implicitly_wait(5)
# checkPopUp(driver)
table = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "section.statistics")))
WebDriverWait(driver, 10).until(EC.visibility_of(table))
items = WebDriverWait(table, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
for i in items:
    print(i.text)

time.sleep(20)

