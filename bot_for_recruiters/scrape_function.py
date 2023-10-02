import asyncio
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup

async def scrape_url(url):
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        element_present = EC.presence_of_element_located((By.TAG_NAME, 'p'))
        WebDriverWait(driver, 20).until(element_present)

        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')

        # Add your scraping logic here

        return soup

    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None
    finally:
        driver.quit()
