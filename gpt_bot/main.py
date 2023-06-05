      # '/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[1]/div[1]/div/label/input'

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# Instantiate the webdriver
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://chat.openai.com/')
time.sleep(10)
try:#                                                                             /html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[1]/div[1]/div/label/input
#     captcha= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[1]/div[1]/div/label/input')))
    captcha=driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/div/div[1]/table/tbody/tr/td[1]/div[1]/div/label/input')
    captcha.click()
    
except Exception as e:
    print(e)
    print('PROBLEM with CAPTCHA')
time.sleep(10)
try:
      send_text=WebDriverWait(driver,20).until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[1]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea'))
      send_text.send_keys('give me short overwiev about the " " job roles in dutch')
except:

     print('could not find a key')
try:
    send_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.XPATH, '/html/body/div[1]/div[2]/div[2]/main/div[2]/form/div/div[2]/button/svg'))
    send_button.click()
except:
     print('problem with send button')
try:
    res=WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.XPATH,'/html/body/div[1]/div[2]/div[2]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/p'))
    print(res.get_text())
except:
     print('Problem with result')