from selenium import webdriver                                      # The base of all
from selenium.webdriver.common.keys import Keys                     # Allow to use keys
from selenium.webdriver.common.by import By                         # Specify selector
from selenium.webdriver.chrome.service import Service               # Generates the browser stuff 
from webdriver_manager.chrome import ChromeDriverManager            # Generates Chrome stuff
from selenium.webdriver.support.ui import WebDriverWait             # Wait tool
from selenium.webdriver.support import expected_conditions as EC    # Specified wait tool

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://google.com')