from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

start = time.time()
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)


def split_intros(links):
    initialScroll = 0
    finalScroll = 1000
    # intros = []    # we can use them to get the user experience and 
    names = []     # user names
    locations = [] # user locations
    k=0
    for i in links:
        print(f'url number --> {k}')
        print(f'url is --> {i}')
        try:
            driver.get(i)
            time.sleep(30)
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
            time.sleep(5)
            try:
                # intro1 = soup.find_all('section', attrs={'class': 'artdeco-card ember-view relative break-words pb3 mt2'})
                # intros.append(intro1)
                # time.sleep(5)                                            
                location_loc = soup.find("span", {'class': 'text-body-small inline t-black--light break-words'}).get_text()
                locations.append(location_loc.strip('\n, " "'))

                name = soup.find("h1", {'class': 'text-heading-xlarge inline t-24 v-align-middle break-words'}).get_text()
                names.append(name)
                works_at_loc = soup.find("div", {'class': 'text-body-medium'})
 
                # this gives us the HTML of the tag in which the Company Name is present
                # Extracting the Company Name
                works_at = works_at_loc.get_text().strip()
                print(f"Works at:-->{works_at_loc.get_text().strip()}")
                print(name)
                print(location_loc.strip('\n, " "'))
            except Exception as e:
                print(e)
                pass
        except Exception as e:
            print(e)
        k+=1
    # df_intros_MATH = pd.DataFrame({
    #     "intros":intros
    # })
    # df_names_MATH = pd.DataFrame({
    #     "names":names
    # })
    # df_locations_MATH = pd.DataFrame({
    #     "locations":locations
    # })
    # # df_intros_MATH.to_csv("intros_MATH_300.csv")
    # df_names_MATH.to_csv("names_MATH_last.csv")
    # df_locations_MATH.to_csv("locations_MATH_last.csv")
    driver.close()
    print(names)
    print(locations)

    return  names, locations #intros
    