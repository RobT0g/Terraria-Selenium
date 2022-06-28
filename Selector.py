import enum
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from Register import Weapon
from openpyxl import Workbook, load_workbook
from Database import Database

db = Database()

class SelectorOfWeapons:
    def __init__(self) -> None:
        self.baseURL = 'https://terraria.fandom.com/wiki/'
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
        last = ''
        for i in re.split('\n', l.text)[1:-1]:
            t = re.findall('[A-Za-z\s-]+', i)[0].strip()
            if(len(num := (re.findall('[\d.]+', i)[0])) == 1):
                self.weaponsTypes[t] = []
                last = t
            else:
                self.weaponsTypes[last].append([t, num])
                self.typeList.append([t, num])
        #db.uploadSections(self.weaponsTypes)
    
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
                    for k1, v1 in enumerate(items):
                        try:
                            weapon = self.getStats(v1)
                        except:
                            weapon = {'nome': v1.text}
                            for i in Weapon.getStats():
                                weapon[i] = None
                        if type(self.weapons[self.typeList[ind][1]]) is list:
                            self.weapons[self.typeList[ind][1]].append(weapon)
                        else:
                            self.weapons[self.typeList[ind][1]][headers[k]].append(weapon)
            except:
                pass
        #db.uploadWeapons(self.weapons)
    
    def getStats(self, element):
        p = self.driver.current_window_handle
        try:
            print(element.text)
            info = {'nome': element.text}
            for i in Weapon.getStats():
                info[i] = None
            link = WebDriverWait(element, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'a'))).get_attribute('href')
            self.driver.execute_script(f'''window.open('{link}');''')
            self.driver.switch_to.window(self.driver.window_handles[1])
            table = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'section.statistics')))
            self.waitLoad(table)
            items = WebDriverWait(table, 5).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
            for i in items:
                try:
                    field = WebDriverWait(i, 5).until(EC.presence_of_element_located((By.TAG_NAME, "th"))).text
                    if field in Weapon.getStats():
                        if field == 'Rarity':
                            try:
                                rarity = WebDriverWait(WebDriverWait(i, 5).until(EC.presence_of_element_located(
                                    (By.TAG_NAME, 'td'))), 5).until(EC.presence_of_element_located((By.TAG_NAME, 'a'))).get_attribute('title')
                                info[field] = re.compile(r'\d+').search(rarity).group()
                            except Exception as e: print(e)
                        else:
                            info[field] = re.compile(r'\d+').search(WebDriverWait(i, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'td'))).text).group()
                except Exception as e: print(e)
            print(info)
            self.driver.close()
            self.driver.switch_to.window(p)
            return info
        except:
            self.driver.close()
            self.driver.switch_to.window(p)
            info = {'nome': element.text}
            for i in Weapon.getStats():
                info[i] = None
            return info

    def waitLoad(self, element, driver = True):
        if driver == True:
            driver = self.driver
        WebDriverWait(driver, 5).until(EC.visibility_of(element))
    
    def finish(self):
        self.driver.quit()

class SelectorOfTools:
    def __init__(self) -> None:
        self.baseURL = 'https://terraria.fandom.com/wiki/'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://terraria.fandom.com/wiki/Tools')
        self.driver.implicitly_wait(5)
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.checkPopUp()
        self.selectTypes()
        self.selectTools()
    
    def checkPopUp(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "NN0_TB_DIsNmMHgJWgT7U.XHcr6qf5Sub2F2zBJ53S_"))).click()
        except:
            pass

    def selectTypes(self):
        self.toolTypes = []
        l = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mw-headline")))
        for i in l:
            self.waitLoad(i)
            if i.text not in ['Miscellaneous', 'Multi-use tools']:
                self.toolTypes.append(i.text)
    
    def selectTools(self):
        self.tools = [[] for i in self.toolTypes]
        l = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "itemlist.terraria")))
        for k, i in enumerate(l):
            self.waitLoad(i)
            tools = WebDriverWait(i, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "i")))
            for j in tools:
                self.tools[k].append(j.text)
    
    def waitLoad(self, element, driver = True):
        if driver == True:
            driver = self.driver
        WebDriverWait(driver, 5).until(EC.visibility_of(element)) 

    def getExcCoord(self, coord):
        if coord[0] > 26:
            return f'{self.alphabet[int(coord[0]/26)]}{self.alphabet[coord[0]%26]}{coord[1]}'
        return f'{self.alphabet[coord[0]%26]}{coord[1]}'

    def saveOnExcel(self):
        table = Workbook()
        act = table.active
        act.append(self.toolTypes)
        for k1, v1 in enumerate(self.tools):
            for k2, v2 in enumerate(v1):
                print(p:=self.getExcCoord((k1, 2+k2)))
                act[p] = v2
        table.save('Base.xlsx')

    def finish(self):
        self.driver.quit()