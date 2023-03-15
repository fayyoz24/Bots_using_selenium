from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
# options = Options()
# options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
# driver = webdriver.Chrome(options=options)
# driver.get('https://www.google.com/search?q=site:linkedin.com/in/+AND+%22Mathematics%22+AND+%22Bachelor%27s&sxsrf=ALiCzsbOTqrA98wDQf3mtEB03kA_O7eCbQ:1668686082134&ei=AiF2Y4vwB-3JrgS9gpd4&start=50&sa=N&ved=2ahUKEwiL-aqJlLX7AhXtpIsKHT3BBQ84KBDy0wN6BAgBEA0&biw=920&bih=625&dpr=1')
# time.sleep(20)




start = time.time()
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)

def comp_univer_degree(intros):
    degree_studie = [] 
    university    = []
    job_type      = [] 
    companies     = [] 

    for i in intros: #len(intros)
        print(intros.index(i))  # number of intro
        # if the length of intro less than three it means lack of data, so we don't need it
        if 3 < len(i):
            k = 2 
            if len(i) > 5: # if itnro length grater than 5, user have 'About' section
                k = 3 
            exps = i[k].find_all("span", {'class': 't-14 t-normal'})
            a = []
            for exp in exps:
                for j in [i[: len(i)//2] for i in [exp.get_text().strip()]]:
                    a.append(j)
                # [exp.get_text().strip()]
            degree_studie.append(a)

            univers = i[k].find_all("span", {'class': 'mr1 hoverable-link-text t-bold'})
            b = []
            for univer in univers:
                for j in [i[: len(i)//2] for i in [univer.get_text().strip()]]:
                    b.append(j)
            university.append(b)

            q = 1
            if len(i) > 5:
                q = 2
            job_typ = i[q].find_all("span", {'class': 'mr1 t-bold'})
            c = []
            for job in job_typ:
                for j in [i[: len(i)//2] for i in [job.get_text().strip()]]:
                    c.append(j)
            job_type.append(c)

            comps = i[q].find_all("span", {'class': 't-14 t-normal'})
            d = []
            for com in comps:
                for j in [i[: len(i)//2] for i in [com.get_text().strip()]]:
                    d.append(j)
            companies.append(d)
        else :
            degree_studie.append([])
            university.append([])
            job_type.append([]) 
            companies.append([]) 
    
    print(degree_studie) 
    print(university)    
    print(job_type)      
    print(companies) 

    # df_degree_study_MATH = pd.DataFrame({
    #     "degree_study":degree_studie
    # })
    # df_university_MATH = pd.DataFrame({
    #     "University":university
    # })
    # df_job_type_MATH = pd.DataFrame({
    #     "job_type":job_type
    # })
    # df_company_MATH = pd.DataFrame({
    #     "company":companies
    # })
    # df_degree_study_MATH.to_csv("degree_study_MATH_300.csv")
    # df_university_MATH.to_csv("university_MATH_300.csv")
    # df_job_type_MATH.to_csv("job_type_MATH_200_300.csv")
    # df_company_MATH.to_csv("company_MATH_300.csv")
    return degree_studie, university, job_type, companies
