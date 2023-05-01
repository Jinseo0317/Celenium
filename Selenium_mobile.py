from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

mobile_emulation = {"deviceName": "iPhone SE"}

options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome("C:\Chrome_Driver\chromedriver.exe", chrome_options=options)

driver.get("https://www.naver.com")
