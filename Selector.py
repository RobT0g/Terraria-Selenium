from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

class SelectorOfWeapons:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://terraria.fandom.com/wiki/Weapons')
        self.driver.implicitly_wait(5)
        self.checkPopUp()
        self.genTypes()
        self.genWeapons()
    
    def checkPopUp(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_"))).click()
        except:
            pass

    def genTypes(self):
        self.weaponsTypes = {}
        l = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "toc")))
        self.waitLoad(l)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of(l))
        last = ''
        for i in re.split('\n', l.text)[1:-1]:
            t = re.findall('[A-Za-z\s-]+', i)[0].strip()
            if(len(re.findall('[\d.]+', i)[0]) == 1):
                self.weaponsTypes[t] = []
                last = t
            else:
                self.weaponsTypes[last].append(t)
    
    def genWeapons(self):
        # AQUI VAI TER QUE USAR UM TRY JÁ QUE NEM TODAS AS LISTAS TEM UM PADRÃO CERTINHO
        self.weapons = {}
        lists = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "infocard.clearfix.terraria.compact")))
        for e in lists:
            self.waitLoad(e)
            titles = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main-heading")))
            for i in titles:
                # self.waitLoad(i)
                pass
    
    def waitLoad(self, element, driver = True):
        if driver == True:
            driver = self.driver
        WebDriverWait(driver, 10).until(EC.visibility_of(element))
    
    def finish(self):
        self.driver.quit()


wp = SelectorOfWeapons()
print(wp.weapons)
wp.finish()
