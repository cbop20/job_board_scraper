from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from opportunity import Opportunity

url = "https://www.builtincolorado.com/jobs/dev-engineering/entry-level/mid-level"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)
oppurtunities = []


while True:
    the_big_cheeses = driver.find_elements(By.XPATH, ('//div[@data-id="job-card"]'))
    for cheese in the_big_cheeses:
        id_company_parent = cheese.find_element(By.XPATH,('.//div[@data-id="company-title"]'))
        id = id_company_parent.get_attribute('data-builtin-track-job-id')
        drop_data = driver.find_element(By.XPATH,(f".//div[@data-job-id='{id}']"))
        company = id_company_parent.find_element(By.XPATH,('./span')).text
        job_info_elements = drop_data.find_elements(By.XPATH,('.//span'))
        job_info = []
        for i in job_info_elements:
            info = i.text
            if info:
                job_info.append(info)
        
        title_href_parent = cheese.find_element(By.XPATH,('.//a[@id="job-card-alias"]'))
        title = title_href_parent.text
        href = title_href_parent.get_attribute('href')
        oppurtunities.append(Opportunity(company,title,href,job_info))
    for o in oppurtunities:
        print(o)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    try:
        next_page_link = driver.find_element(By.XPATH,'//a[@aria-label="Go to Next Page"]')
        driver.execute_script('arguments[0].click();', next_page_link)
    except:
        break
driver.quit()
print("Done")