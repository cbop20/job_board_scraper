
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from opportunity import Opportunity
url = "https://www.indeed.com/jobs?q=software&l=Denver%2C+CO&sc=0kf%3Aexplvl%28ENTRY_LEVEL%29%3B&radius=15&vjk=6da7a4cdaf49c7c8"
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
opportunities = []
while True:
    the_big_cheeses = driver.find_elements(By.CLASS_NAME,'resultContent')
    for cheese in the_big_cheeses:
        link_title = cheese.find_element(By.XPATH,'.//a[starts-with(@aria-label,"full details")]')
        link = link_title.get_attribute('href')
        title = link_title.find_element(By.XPATH,'./span').text
        company = cheese.find_elements(By.XPATH,'.//span[@data-testid="company-name"]')
        if(len(company)>0):
            company = company[0].text
        else:
            company = ""
        job_info_elements = cheese.find_elements(By.XPATH, './/div[@data-testid="attribute_snippet_testid"]')
        opportunities.append(Opportunity(company,title,link,[info.text for info in job_info_elements]))
    for o in opportunities:
        print(o)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    try:
        next_page_link = driver.find_element(By.XPATH,'//a[@aria-label="Next Page"]')
        driver.execute_script('arguments[0].click();', next_page_link)
    except:
        break
driver.quit()
print("Done")