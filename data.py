from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


# options.add_argument("user-data-dir=C:\ProgramData\Microsoft\Windows\Start Menu\Programs")
options = Options()
options.add_argument("user-data-dir=C:\\Users\\dell")
# driver=webdriver.Chrome(executable_path="Bots_using_selenium\chromedriver.exe")
driver = webdriver.Chrome(options=options)
driver.get('https://www.crystalknows.com/app/ce/installed')
time.sleep(15)
import pandas as pd
list_studies=['math', 'art-history', 'biochemistry', 'biology', 'biomedical-science','chemistry',
              'computer-science','english-literature', 'history', 'physics']
for study in list_studies:
    dict_={}
    df = pd.read_csv(f'datas/linkedin_aaccount_links/{study}.csv')
    i=0
    for link in df.links[10:]:
        i+=1
        try: 
            link_enterong_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/nav/div/div[1]/div/div[1]/div/input')
            link_enterong_button.click()
            link_enterong_button.clear()
            link_enterong_button.send_keys(link)
            time.sleep(8) 
        except Exception as e:
            print("problem account")
        try:                          # /html/body/div[2]/div/div/div[2]/div[1]/nav/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]
            first_user=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/nav/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]')
            first_user.click()
            time.sleep(10)
            src = driver.page_source
            soup = BeautifulSoup(src, 'lxml')
            cs=soup.find('div', {'class':'styles_disc-pill-wrapper__aB3OJ'})
            # print(cs.text.strip())              
            math_cs[link]=cs.text.strip()       #styles_quality__dm_So styles_DI__sElCv
            # print(cs.text.strip())              #styles_container__BY0sl
        except Exception as e:
            math_cs[link]='nan'
            continue
        if i%10==0:
            try:
                dots=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/nav/div/div/div/div[6]/div/div[1]/div[2]/div/div/div')
                dots.click()
                time.sleep(2)
                logout=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/nav/div/div/div/div[6]/div/div[2]/div[6]/a')
                logout.click()
                time.sleep(5)
                signup=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div[3]/div/form/div[3]/div/a')
                signup.click()
                time.sleep(8)
                try:
                    cookies_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div')
                    cookies_button.click()
                    time.sleep(2)
                    signup_button=driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/nav/div/div/div[2]')
                    signup_button.click()
                except Exception as e:
                    print('Cookie button not found!')
                try:
                    first_name_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div/div[3]/form/div/div[2]/div[1]/input')
                    first_name_input.click()
                    first_name_input.send_keys(f'Alibek+{str(i)}')
                except Exception as e:
                    print('first_name-->problem')
                try:
                    last_name_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div/div[3]/form/div/div[2]/div[2]/input')
                    last_name_input.click()
                    last_name_input.send_keys(f'Aliyev{str(i)}')
                except Exception as e:
                    print('last_name-->problem')
                try:
                    comp_email_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div/div[3]/form/div/div[3]/div/input')
                    comp_email_input.click()
                    comp_email_input.send_keys(f'{study[:2]}{str(i)}@a.com')
                except Exception as e:
                    print('comp_email-->problem')
                try:
                    first_pass_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div/div[3]/form/div/div[4]/div[1]/input')
                    first_pass_input.click()
                    first_pass_input.send_keys('Aa2301667')
                except Exception as e:
                    print('first_pass-->problem')
                try:    
                    sec_pass_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div/div[3]/form/div/div[4]/div[2]/input')
                    sec_pass_input.click()
                    sec_pass_input.send_keys('Aa2301667')
                except Exception as e:
                    print('sec_pass-->problem')
                try:
                    agree_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div/div[3]/form/div/div[5]/div/label/div/img')
                    agree_button.click()
                except Exception as e:
                    print('agree_button-->problem')
                try:
                    signup_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/header/div[2]/div[2]/div/div/div[3]/form/div/div[6]/button')
                    signup_button.click()
                    time.sleep(10)
                except Exception as e:
                    print('signup_button-->problem')
                try:
                    country_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div[2]/img')
                    country_button.click()
                    first_country=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]')
                    first_country.click()
                except Exception as e:
                    print('country_button-->problem')                                # second country    '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/div[2]'

                try:
                    job_title_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/input')
                    job_title_input.click()
                    job_title_input.send_keys('software engineer')
                except Exception as e:
                    print('job_title-->problem')
                try:    
                    my_department_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[2]')
                    my_department_input.click()
                    first_department=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[1]')                              #  second department           '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div[3]/div[2]/div[2]'
                    first_department.click()
                except Exception as e:
                    print('department-->problem')
                try:    
                    my_company_input=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div/input')
                    my_company_input.click()
                    my_company_input.send_keys(f'{study[:2]}')
                    first_company=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div')
                    first_company.click()
                except Exception as e:
                    print('my_company-->problem') 
                try:    
                    next_button=driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/header/div[2]/div[2]/div/div[2]/a')
                    next_button.click()
                    time.sleep(10)
                except Exception as e:
                    print('next_button-->problem')
            except Exception as e:
                print('cannot create new account!')
    df = pd.DataFrame({
    'links':list(dict_.keys()),
    'characters':list(dict_.values())
    })
    df.to_csv(f'datas/cs_values/{study}1.csv', index=False)
                    