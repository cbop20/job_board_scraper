from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
username="calebstarkey@hotmail.com"
password="Cstar101200*"

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
ycombinitiallink = "https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F"

ColoradoLink = "https://www.workatastartup.com/companies?demographic=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=fulltime&layout=list-compact&locations=CO%2C%20US&minExperience=0&minExperience=1&sortBy=created_desc&tab=any&usVisaNotRequired=any"
driver.get(ycombinitiallink)
user_atrib = 'ycid-input'
password_atrib = 'password-input'
username_input = driver.find_element(By.ID, user_atrib)
password_input = driver.find_element(By.ID, password_atrib) 
username_input.send_keys(username)
password_input.send_keys(password)
login = driver.find_element(By.XPATH, '//button[.//span[text()="Log in"]]')
login.click()
try:
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'waas-sidebar-filters'))
    )
except TimeoutError:
    print("Timed out waiting for login load")
driver.get(ColoradoLink)
time.sleep(1)
titles = driver.find_elements(By.XPATH, '//div[@class="job-name"]//a')
for t in titles:
    print(t.text)
time.sleep(15)
# elem = driver.find_elements(By.CLASS_NAME, "job-name")
# for e in elem: print(e.text)

# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
# link = "https://www.ycombinator.com/jobs/location/Colorado"
# driver.get(link)
# titles = driver.find_elements(By.XPATH, 'font-semibold text-linkColor')
# print(titles)
# driver.quit()