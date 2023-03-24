from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import pandas as pd

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)
# 'Mathematics and Bachelor words are used as a default, it is changeble
driver.get('https://www.google.com/search?q=site:nl.linkedin.com/in/+AND+%22Mathematics%22+AND+%22Bachelor%27s+AND+%22Amsterdam&sxsrf=ALiCzsbOTqrA98wDQf3mtEB03kA_O7eCbQ:1668686082134&ei=AiF2Y4vwB-3JrgS9gpd4&start=50&sa=N&ved=2ahUKEwiL-aqJlLX7AhXtpIsKHT3BBQ84KBDy0wN6BAgBEA0&biw=920&bih=625&dpr=1')
time.sleep(10) # to make slower 

def URLget(n): # n is the number of pages
    links = [] # save links here
    while n > 0:
        time.sleep(5)
        for i in range(1, 11): # google uses paginator, every page has 10 urls
            time.sleep(6)
            try:
                elems = driver.find_elements(By.XPATH, '//*[@id="rso"]/div['+str(i)+']/div/div/div[1]/div/a')
                for elem in elems:
                    
                    clean_url = elem.get_attribute("href") # extracting url 
                    base_url = "linkedin.com/in/"
                    if clean_url.find(base_url) != -1 and '%' not in clean_url: # sometimes google gives no Ln urls, so clean it
                        links.append(clean_url)
                        print(f"url is --->{clean_url}")
            except Exception as e:
                print(e)
                pass
        try:
            next_button = driver.find_element(By.XPATH, '//*[@id="pnnext"]') # clicking next button 
            next_button.click()
        except Exception as e:
            print(e)
        print(f'{n} pages left!')
        n -= 1
    # df = pd.DataFrame({
    #     "links":links
    # })
    # df.to_csv('links_22_02_23.csv')
    # driver.close()
    return links

for q in range(7,10):
    links = URLget(25)
    df = pd.DataFrame({
        "links":links
    })
    print(f"qqqq-->{q}")
    df.to_csv(f'links_22_02_23_{q}.csv')
    # driver.close()
# URLget(25)