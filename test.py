from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options=options
driver = webdriver.Chrome("C:/Users/82107/Desktop/크롤링 보조도구/로고아카이브/chromedriver")
url='https://www.google.com/doodles?hl=ko#archive'
driver.get(url)
result=driver.find_elements(By.CSS_SELECTOR, '#latest-ul > li.latest-doodle > div > div > input.title')
for t in result:
    print(t.get_attribute('value'))
