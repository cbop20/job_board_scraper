
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
def IndeedScrape(db_connection,db_cursor, headless, insert_script):
    print("Starting Indeed scrape.")
    try:
        url = os.getenv('INDEED_LINK')
        options = webdriver.ChromeOptions()
        if(headless):
            options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
    except Exception as ex:
        print("Getting initial link failed.")
        return
    
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
            job_info = []
            for i in job_info_elements:
                info = i.text
                if info:
                    job_info.append(info)
            
            db_cursor.execute(insert_script, (company,title,link,job_info))
        try:
            db_connection.commit()
            next_page_link = driver.find_element(By.XPATH,'//a[@aria-label="Next Page"]')
            driver.execute_script('arguments[0].click();', next_page_link)
        except:
            break
    driver.quit()
    print("Indeed scraper done")