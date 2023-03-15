def get_datas_as_list(li_s):

    images=[]
    salaries=[]
    companies=[]
    job_titles=[]
    locations=[]

    for pro in li_s:
        try:
            image=pro.find('img')['src']
            images.append(image)
        except Exception as e:
            print(f"images_error--> {e}")
            images.append("nan")
        try:
            salary=pro.find('span', {"data-test":"detailSalary"}).text.strip()
            salaries.append(salary)
        except Exception as e:
            print(f"salaries_error--> {e}")
            salaries.append("nan")
        try:
            company=pro.find('a', {"class":"css-l2wjgv e1n63ojh0 jobLink"}).text.strip()
            companies.append(company)
        except Exception as e:
            print(f"companies_error--> {e}")
            companies.append("nan")
        try:
            job=pro.find('a', {"class":"jobLink css-1rd3saf eigr9kq2"}).text.strip()
            job_titles.append(job)
        except Exception as e:
            print(f"job_titles_error--> {e}")
            job_titles.append("nan")
        try:
            loc=pro.find('span', {"data-test":"emp-location"}).text.strip()
            locations.append(loc)
        except Exception as e:
            print(f"locations_error--> {e}")
            locations.append("nan")

    return companies, images, locations, job_titles, salaries