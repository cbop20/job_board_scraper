from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
import os

def YCombScraper(db_connection,db_cursor, headless, insert_script):
    print("Starting YComb scrape.")
    options = webdriver.ChromeOptions()
    if(headless):
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    login_link = os.get("Y_COMB_LOGIN_LINK")

    state_link = os.get("Y_COMB_STATE_LINK")
    remote_link = os.get("Y_COMB_REMOTE_LINK")
    links = [state_link,remote_link]
    
    driver.get(login_link)

    config = configparser.ConfigParser()
    config.read('../.config.ini')

    user_atrib = 'ycid-input'
    password_atrib = 'password-input'
    username_input = driver.find_element(By.ID, user_atrib)
    password_input = driver.find_element(By.ID, password_atrib) 
    username_input.send_keys(os.getenv('Y_COMB_EMAIL'))
    password_input.send_keys(os.getenv('Y_COMB_PASSWORD'))
    login = driver.find_element(By.XPATH, '//button[.//span[text()="Log in"]]')
    login.click()
    try:
        WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.ID,'waas-sidebar-filters'))
        )
    except TimeoutError:
        print("Timed out waiting for login load")

    for link in links:
        driver.get(link)
        wait = WebDriverWait(driver, 10)
        time.sleep(5)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        the_medium_cheese = driver.find_elements(By.XPATH,'//div[@class="mb-4 flex flex-col justify-between sm:flex-row"]')
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
            db_cursor.execute(insert_script, (None,title,link,job_info))
        db_connection.commit()
    driver.quit()