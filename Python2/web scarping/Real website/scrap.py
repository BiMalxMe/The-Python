from bs4 import BeautifulSoup
import requests
import time



print(" Put one skill you are unfamiliar with ")
unfamiliar_skill=input('>')
print(f"filtering Out {unfamiliar_skill}")


def find_jobs():
    html_page=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup=BeautifulSoup(html_page,'lxml')
    jobs=soup.findAll('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').text
        if 'few' in published_date:

            Company_name=job.find('h3',class_='joblist-comp-name').text.replace('  ','')
            skill=job.find('span',class_='srp-skills').text.replace('  ','')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skill:
                with open(f'posts/{index}.txt','w') as f:
# company skill ani indo print garni

                    f.write(f'Company Name = {Company_name.strip()}\n')
                    f.write(f'Required Skills = {skill.strip()}\n')
                    f.write(f'More information = {more_info}\n')
                print(f"File {index}.txt saved")
                    
    
if __name__=="__main__":
    while True:
        find_jobs()
        time.wait=10
        print(f"Waiting {time.wait} minutes")
        time.sleep(time.wait*60)
