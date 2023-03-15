from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# options = Options()
# options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
# driver = webdriver.Chrome(options=options)
# site = "https://www.glassdoor.com/Reviews/ING-Netherlands-Reviews-EI_IE4264.0,3_IL.4,15_IN178.htm?filter.iso3Language=nld"
# driver.get(site)
# time.sleep(20)
# initialScroll = 0
# finalScroll = 1000
# start = time.time()
# while True:
#     driver.execute_script(f"window.scrollTo({initialScroll}, {finalScroll})")
#     initialScroll = finalScroll
#     finalScroll += 1000
#     time.sleep(3)
#     end = time.time()
#     if round(end - start) > 20:
#         break
# src = driver.page_source
# soup = BeautifulSoup(src, 'lxml')
# # Pros_s=driver.find_elements(By.XPATH, '//*[@id="empReview"]/div/div/div[2]/div/div[2]/div[1]/p[2]/span')

# Pros_s=soup.find_all('p',{'class':"mt-0 mb-0 pb v2__EIReviewDetailsV2__bodyColor v2__EIReviewDetailsV2__lineHeightLarge v2__EIReviewDetailsV2__isCollapsed "})
# print(Pros_s)                 #//*[@id="empReview_68686222"]/div/div/div[2]/div/div[2]/div[1]/p[2]/span
# for pro in Pros_s:
#     print(pro)
# a =soup.find_all('p', {'class':"mt-0 mb-0 pb v2__EIReviewDetailsV2__bodyColor v2__EIReviewDetailsV2__lineHeightLarge v2__EIReviewDetailsV2__isCollapsed"})
# print(a)
# b=driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/main/div[5]/div/ol/li[10]/div/div/div[2]/div/div[2]/div[1]/p[2]/span")

# list_pros=[]
# for i in a:
#     try:
#         print(i.find('span', {'data-test':"pros"}).text.strip())
#         list_pros.append(i.find('span', {'data-test':"pros"}).text.strip())
#     except Exception as e:
#         print(e)

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)

# driver.get(site)
def get_glassdoor_reviews(site):
    driver.get(site)
    time.sleep(20)
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
    # Pros_s=driver.find_elements(By.XPATH, '//*[@id="empReview"]/div/div/div[2]/div/div[2]/div[1]/p[2]/span')

    # Pros_s=soup.find_all('p',{'class':"mt-0 mb-0 pb v2__EIReviewDetailsV2__bodyColor v2__EIReviewDetailsV2__lineHeightLarge v2__EIReviewDetailsV2__isCollapsed "})
    # print(Pros_s)                 #//*[@id="empReview_68686222"]/div/div/div[2]/div/div[2]/div[1]/p[2]/span
    # for pro in Pros_s:
    #     print(pro)
    a =soup.find_all('p', {'class':"mt-0 mb-0 pb v2__EIReviewDetailsV2__bodyColor v2__EIReviewDetailsV2__lineHeightLarge v2__EIReviewDetailsV2__isCollapsed"})
    # print(a)

    list_pros=[]
    for pro in a:
        try:
            print(pro.find('span', {'data-test':"pros"}).text.strip())
            list_pros.append(pro.find('span', {'data-test':"pros"}).text.strip())
        except Exception as e:
            print(e)
    list_cons=[]
    for con in list_cons:
        try:
            print(con.find('span', {'data-test':"cons"}).text.strip())
            list_pros.append(con.find('span', {'data-test':"cons"}).text.strip())
        except Exception as e:
            print(e)

    df=pd.DataFrame({
        "pros":list_pros,
        "cons":list_cons
    })
    df.to_csv("ING_pros_cons.csv", index=False)
site = "https://www.glassdoor.com/Reviews/ING-Netherlands-Reviews-EI_IE4264.0,3_IL.4,15_IN178.htm?filter.iso3Language=nld"
get_glassdoor_reviews(site)