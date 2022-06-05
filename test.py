from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

driver = set_chrome_driver()

url='https://www.google.com/doodles?hl=ko#archive'
driver.get(url)
result=driver.find_elements(By.CSS_SELECTOR, '#latest-ul > li.latest-doodle > div > div > input.title')
for t in result:
    print(t.get_attribute('value'))

images_url = []

for i in range(1,7):
    images = driver.find_element(By.CSS_SELECTOR, f"#archive-list > li:nth-child({i}) > div.thumb-container > div.thumb-image > a > img")
    images_url.append(images)

img_url = []

for image in images_url :
    url = image.get_attribute('src')
    img_url.append(url)

for ed in img_url:
    print(ed)




img_folder = './Desktop/crawling_selenium'

if not os.path.isdir(img_folder) :
    os.mkdir(img_folder)

for index, link in enumerate(img_url) :
    urlretrieve(link, f'./img/{index}.jpg')

driver.quit()
