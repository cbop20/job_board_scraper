from selenium import webdriver
import os 
import logging
class Scrape:
    def __init__(self,db_con,db_cursor,headless,insert_script):
        self.db_con = db_con
        self.db_cursor = db_cursor
        self.insert_script = insert_script
        try:
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Remote(
                command_executor='http://chrome:4444/wd/hub',
                options=options)
        except Exception as ex:
            logging.info(ex)
    
    def scrape(self):
        print("Scrape")
        return
    
