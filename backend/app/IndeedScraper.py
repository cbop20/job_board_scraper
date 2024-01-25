from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app import Scraper
import os
import time
class IndeedScrape(Scraper.Scrape):
    def __init__(self,db_con,db_cursor,headless,insert_script):
        super().__init__(db_con,db_cursor,headless,insert_script)
    
    def scrape(self):
        print("Starting Indeed scrape.")
        try:
            url = os.getenv('INDEED_LINK')
            self.driver.get(url)
        except Exception as ex:
            print("Getting initial link failed.")
            return
        while True:
            the_big_cheeses = self.driver.find_elements(By.CLASS_NAME,'resultContent')
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
                
                self.db_cursor.execute(self.insert_script, (company,title,link,job_info))
            try:
                self.db_con.commit()
                WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.XPATH,'//a[@aria-label="Next Page"]'))
                )
                next_page_link = self.driver.find_element(By.XPATH,'//a[@aria-label="Next Page"]')
                self.driver.execute_script('arguments[0].click();', next_page_link)
            except:
                break
        time.sleep(100)
        # self.driver.quit()
        print("Indeed scraper done")