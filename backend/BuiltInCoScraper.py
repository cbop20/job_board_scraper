from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
def BuiltInScrape(db_connection,db_cursor, headless, insert_script):
    print("Starting BuiltIn scrape.")
    try:
        url = os.getenv('BUILTIN_LINK')
        options = webdriver.ChromeOptions()
        if(headless):
            options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
    except Exception as ex:
        print("Getting initial link failed.")
        return

    wait = WebDriverWait(driver, 10)

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
            link = title_href_parent.get_attribute('href')
            db_cursor.execute(insert_script, (company,title,link,job_info))
        try:
            db_connection.commit()
            next_page_link = driver.find_element(By.XPATH,'//a[@aria-label="Go to Next Page"]')
            driver.execute_script('arguments[0].click();', next_page_link)
        except:
            break
        
    driver.quit()
    print("BuiltInCo scraper done")