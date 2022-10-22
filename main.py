import os
from selenium import webdriver

driver_path = r'C:\SeleniumDrivers'
os.environ['PATH'] += driver_path



driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/')
