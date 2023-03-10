from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('http://quotes.toscrape.com/login')

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'username')))

login = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')

# Ввод данных в необходимые поля
login.send_keys('admin')
password.send_keys('admin')

# После ввода данных логина и пароля, нажимаем кнопку
login_btn = driver.find_element(By.XPATH, "//input[@value='Login']")
login_btn.click()

# Ожидаем получения определенного элемента
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'quote')))

html = driver.page_source
print(html)

driver.quit()
