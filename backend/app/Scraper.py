from selenium import webdriver
import os 
class Scraper:
    def __init__(self,db_con,db_cursor,headless,insert_script):
        self.db_con = db_con
        self.db_cursor = db_cursor
        self.insert_script = insert_script

        options = webdriver.ChromeOptions()
        if(headless):
            options.add_argument('--headless')
        user_agent = os.getenv('CONNECTION_STRING')
        options.add_argument(f'user-agent={user_agent}')
        self.driver = webdriver.Chrome(options=options)
    
    def scrape(self):
        print("Scrape")
    
