
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.indeed.com/jobs?q=software&l=Denver%2C+CO&sc=0kf%3Aexplvl%28ENTRY_LEVEL%29%3B&radius=15&vjk=6da7a4cdaf49c7c8"
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
elements = driver.find_elements(By.CSS_SELECTOR,'span[id^="jobTitle"]')
for e in elements:
    print(e.text)
next_page_link = driver.find_element(By.XPATH,'//a[@aria-label="Next Page"]')
while next_page_link:
    next_page_link.click()
    elements = driver.find_elements(By.CSS_SELECTOR,'span[id^="jobTitle"]')
    for e in elements:
        print(e.text)
    next_page_link = driver.find_element(By.XPATH,'//a[@aria-label="Next Page"]')
time.sleep(3)
driver.quit()
# elem = driver.find_elements(element_type, element_field)
# for e in elem: print(e.text)
# driver.quit()