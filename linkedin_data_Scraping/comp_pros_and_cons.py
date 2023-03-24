from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
def get_pros():
    pros=[]
    cons=[]
    df=pd.read_csv('./linkedin_data_Scraping/history_csv/history_education.csv')
    companies=df.companies
    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
    driver = webdriver.Chrome(options=options)
    site = "https://www.glassdoor.com/Search/results.htm?keyword=&locId=178&locT=N&locName=Netherlands"

    for comp in companies:
        driver.get(site)
        time.sleep(20)                         
        comp_input=driver.find_element(By.XPATH, '//*[@id="sc.keyword"] ')  
        time.sleep(5)
        comp_input.click()
        comp_input.clear()
        comp_input.send_keys(comp)
        time.sleep(5)
        try:
            search_button=driver.find_element(By.XPATH, '//*[@id="scBar"]/div/button')
            search_button.click()
            time.sleep(5)

            first_comp=driver.find_element(By.XPATH, '//*[@id="Discover"]/div/div/div[1]/div[1]/div[1]/a[1]')
            first_comp.click()
            time.sleep(5)
                                                                #eiCell cell reviews 
            comp_review_button=driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div/div[1]/article[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/a[1]')
            comp_review_button.click()
            time.sleep(5)
            
            initialScroll = 0                    
            finalScroll = 1000
            start = time.time()
            while True:
                driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
                initialScroll = finalScroll
                finalScroll += 1000
                time.sleep(3)
                end = time.time()
                if round(end - start) > 20:
                    break
            src = driver.page_source
            soup = BeautifulSoup(src, 'lxml')

            a =soup.find_all('p', {'class':"mt-0 mb-0 pb v2__EIReviewDetailsV2__bodyColor v2__EIReviewDetailsV2__lineHeightLarge v2__EIReviewDetailsV2__isCollapsed"})
            
            list_cons=[]
            list_pros=[]
            for i in a:
                try:
                    list_cons.append(i.find('span', {'data-test':"cons"}).text.strip())
                except Exception as e:
                    print(e)
            for i in a:
                try:
                    list_pros.append(i.find('span', {'data-test':"pros"}).text.strip())
                except Exception as e:
                    print(e)
            if len(list_cons)==0:
                list_cons.append('NG')
            if len(list_pros)==0:
                list_pros.append('NG')

            pros.append(list_pros)
            cons.append(list_cons)
        except Exception as e:
            print(e)
            pros.append("NG")
            cons.append("NG")
    # driver.close()
get_pros()