import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://terraria.fandom.com/wiki/Weapons')
driver.implicitly_wait(5)
driver.execute_script(f"window.open('https://terraria.fandom.com/wiki');")
driver.execute_script(f"window.open('https://terraria.fandom.com/wiki/Tools');")
driver.execute_script(f"window.open('https://terraria.fandom.com/wiki/House');")
p = driver.current_window_handle

#get first child window
chwd = driver.window_handles

for k, w in enumerate(chwd):
#switch focus to child window
    if(w!=p):
        print(k, w)
        driver.switch_to.window(w)
        time.sleep(3)
# driver.close()
time.sleep(20)

