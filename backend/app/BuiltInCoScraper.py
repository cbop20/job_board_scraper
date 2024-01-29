from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app import Scraper
import os
import logging

class BuiltInScrape(Scraper.Scrape):
    def __init__(self,db_con,db_cursor,headless,insert_script):
        super().__init__(db_con,db_cursor,headless,insert_script)
    
    def scrape(self):
        logging.info("Starting BuiltIn scrape.")
        try:
            url = os.getenv('BUILTIN_LINK')
            self.driver.get(url)
        except Exception as ex:
            logging.info("Getting initial link failed.")
            return
        while True:
            the_big_cheeses = self.driver.find_elements(By.XPATH, ('//div[@data-id="job-card"]'))
            for cheese in the_big_cheeses:
                id_company_parent = cheese.find_element(By.XPATH,('.//div[@data-id="company-title"]'))
                id = id_company_parent.get_attribute('data-builtin-track-job-id')
                drop_data = self.driver.find_element(By.XPATH,(f".//div[@data-job-id='{id}']"))
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
                self.db_cursor.execute(self.insert_script, (company,title,link,job_info))
            try:
                self.db_con.commit()
                next_page_link = self.driver.find_element(By.XPATH,'//a[@aria-label="Go to Next Page"]')
                self.driver.execute_script('arguments[0].click();', next_page_link)
            except:
                break
            
        self.driver.quit()
        logging.info("BuiltInCo scraper done")
        return "sucesss"