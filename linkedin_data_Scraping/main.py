import pandas as pd

# from get_urls_google import URLget
# links = URLget(40)
new_links = pd.read_csv('links_MATH.csv')

from split_intros import split_intros
names, locations = split_intros(links=new_links.links[5:20])

# from comp_univer import comp_univer_degree
# degree_studie, university, job_type, companies = comp_univer_degree(intros=intros)

# def save_csv():
#     df = pd.DataFrame({
#         'Name': names,
#         # 'Link': links,
#         'Location': locations,
#         # 'University': university,
#         # 'Degree and Studie': degree_studie,
#         # 'Company': companies,
#         # 'Job': job_type
#     })

#     df.to_csv('Bachelor_and_Math1_300.csv')

# save_csv()