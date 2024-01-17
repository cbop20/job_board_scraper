from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import configparser
from opportunity import Opportunity
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
ycombinitiallink = "https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F"

ColoradoLink = "https://www.workatastartup.com/companies?demographic=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=fulltime&layout=list-compact&locations=CO%2C%20US&minExperience=0&minExperience=1&sortBy=created_desc&tab=any&usVisaNotRequired=any"
RemoteLink = "https://www.workatastartup.com/companies?demographic=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&remote=only&sortBy=created_desc&tab=any&usVisaNotRequired=any"
driver.get(ycombinitiallink)

config = configparser.ConfigParser()
config.read('../.config.ini')

user_atrib = 'ycid-input'
password_atrib = 'password-input'
username_input = driver.find_element(By.ID, user_atrib)
password_input = driver.find_element(By.ID, password_atrib) 
username_input.send_keys(config.get('YCOMB','YCOMBEMAIL'))
password_input.send_keys(config.get('YCOMB','YCOMBPASSWORD'))
login = driver.find_element(By.XPATH, '//button[.//span[text()="Log in"]]')
login.click()
try:
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'waas-sidebar-filters'))
    )
except TimeoutError:
    print("Timed out waiting for login load")

driver.get(RemoteLink)
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
opportunities = []
the_medium_cheese = driver.find_elements(By.XPATH,'//div[@class="mb-4 flex flex-col justify-between sm:flex-row"]')
for cheese in the_medium_cheese:
    title_link = cheese.find_element(By.XPATH,'.//a')
    title = title_link.text
    link = title_link.get_attribute('href')
    job_info_elements = cheese.find_elements(By.XPATH,'.//div[@class="mr-2 text-sm sm:mr-3 sm:flex sm:flex-wrap"]//span')
    opportunities.append(Opportunity("",title,link,[info.text for info in job_info_elements]))
for o in opportunities:
    print(o)
time.sleep(15)
driver.quit()