from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def get_lis(site):
    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
    driver = webdriver.Chrome(options=options)
    # site = "https://www.glassdoor.com/Job/netherlands-data-scientist-jobs-SRCH_IL.0,11_IN178_KO12,26.htm?industryNId=10012"
            # https://www.glassdoor.com/Reviews/Shell-Reviews-E5833.htm
            # https://www.glassdoor.com/Reviews/ABN-AMRO-Reviews-E10499.htm
            # https://www.glassdoor.com/Reviews/CircleCI-Reviews-E919755.htm
    from selenium.webdriver.common.by import By
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

    li_s=soup.find_all('li',{'class':"react-job-listing css-wp148e eigr9kq3"})
    # print(Pros_s)                 #//*[@id="empReview_68686222"]/div/div/div[2]/div/div[2]/div[1]/p[2]/span
    # for pro in Pros_s:
    #     print(pro)
    return li_s