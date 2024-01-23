from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Scraper import Scraper
import time
import os

class YCombScrape(Scraper):
    def __init__(self,db_con,db_cursor,headless,insert_script):
        super().__init__(db_con,db_cursor,headless,insert_script)
        self.login_link = os.getenv('Y_COMB_LOGIN_LINK')
        self.links = os.getenv('Y_COMB_LINKS', '').split(',')
        self.username = os.getenv('Y_COMB_EMAIL')
        self.password = os.getenv('Y_COMB_PASSWORD')
    def scrape(self):
        print("Starting YComb scrape.")
        
        self.driver.get(self.login_link)

        user_atrib = 'ycid-input'
        password_atrib = 'password-input'
        username_input = self.driver.find_element(By.ID, user_atrib)
        password_input = self.driver.find_element(By.ID, password_atrib) 
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        login = self.driver.find_element(By.XPATH, '//button[.//span[text()="Log in"]]')
        login.click()
        try:
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.ID,'waas-sidebar-filters'))
            )
        except TimeoutError:
            print("Timed out waiting for login load")
        
        for link in self.links:
            self.driver.get(link)
            time.sleep(5)
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            the_medium_cheese = self.driver.find_elements(By.XPATH,'//div[@class="mb-4 flex flex-col justify-between sm:flex-row"]')
            for cheese in the_medium_cheese:
                title_link = cheese.find_element(By.XPATH,'.//a')
                title = title_link.text
                link = title_link.get_attribute('href')
                job_info_elements = cheese.find_elements(By.XPATH,'.//div[@class="mr-2 text-sm sm:mr-3 sm:flex sm:flex-wrap"]//span')
                job_info = []
                for i in job_info_elements:
                    info = i.text
                if info:
                    job_info.append(info)
                self.db_cursor.execute(self.insert_script, (None,title,link,job_info))
            self.db_con.commit()
        self.driver.quit()