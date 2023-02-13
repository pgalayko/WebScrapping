import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://quotes.toscrape.com/scroll')

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'quotes')))

pass_time = 0.5
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(pass_time)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break
    last_height = new_height

quotes = driver.find_elements(By.CLASS_NAME, 'quote')
print(len(quotes))

driver.quit()
