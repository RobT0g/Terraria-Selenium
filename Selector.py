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
        self.typeList = []
        l = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "toc")))
        self.waitLoad(l)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of(l))
        last = ''
        for i in re.split('\n', l.text)[1:-1]:
            t = re.findall('[A-Za-z\s-]+', i)[0].strip()
            if(len(num := (re.findall('[\d.]+', i)[0])) == 1):
                self.weaponsTypes[t] = []
                last = t
            else:
                self.weaponsTypes[last].append([t, num])
                self.typeList.append([t, num])
    
    def genWeapons(self):
        self.weapons = {}
        lists = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "infocard.clearfix.terraria.compact")))
        for ind, e in enumerate(lists):
            self.weapons[self.typeList[ind][1]] = []
            self.waitLoad(e)
            headers = []
            try:
                titles = WebDriverWait(e, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "main-heading")))
                for v in titles:
                    self.waitLoad(v)
                    headers.append(v.text)
                    if not(type(self.weapons[self.typeList[ind][1]]) is dict):
                        self.weapons[self.typeList[ind][1]] = {}
                    self.weapons[self.typeList[ind][1]][v.text] = []
            except:
                pass
            try:
                wpList = WebDriverWait(e, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "itemlist")))
                for k, v in enumerate(wpList):
                    self.waitLoad(v)
                    items = WebDriverWait(v, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "i")))
                    for v1 in items:
                        if type(self.weapons[self.typeList[ind][1]]) is list:
                            self.weapons[self.typeList[ind][1]].append(v1.text)
                        else:
                            self.weapons[self.typeList[ind][1]][headers[k]].append(v1.text)
            except:
                pass
    
    def getStats(self, element):
        pass
    
    def waitLoad(self, element, driver = True):
        if driver == True:
            driver = self.driver
        WebDriverWait(driver, 5).until(EC.visibility_of(element))
    
    def finish(self):
        self.driver.quit()


wp = SelectorOfWeapons()
for v in wp.weapons:
    print(f'{v}\n> {wp.weapons[v]}')
wp.finish()
