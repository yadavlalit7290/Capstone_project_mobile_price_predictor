from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys  import Keys
import time, os

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)


edge_path = "D:\\Campus x\\DSMP\\Paid fees\\12 week\\Slenium\\Chrome Driver\\chromedriver-win64 lates\\chromedriver.exe"

s = Service(edge_path)

driver = webdriver.Chrome(options=options,service=s)

driver.get('https://www.smartprix.com/mobiles')

time.sleep(2)



counter = 0

old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
    time.sleep(2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(2)
    
    print(counter)
    counter = counter + 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = driver.page_source

with open("smartprix_new_2.html",'w',encoding='utf-8') as f:
    f.write(html)


