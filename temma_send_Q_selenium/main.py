import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

df = pd.read_csv('questions.csv')

list_of_questions = df['questions']

driver = webdriver.Chrome(executable_path='chromedriver.exe')
# question_input = driver.find_element_by_class_name('rounded-full bg-gray-200 input p-1 px-2')
for i in range(10, 20):
    try:
        driver.get('https://demo.temma.app/club/list/'+ str(i))
        time.sleep(3)
        for i in range(1):
            question_input = driver.find_element(By.NAME, "question")
            time.sleep(3)
            new_quest = random.choice(list_of_questions)
            question_input.send_keys(new_quest)
            time.sleep(3)
            question_input.submit()
    except:
        pass

    



