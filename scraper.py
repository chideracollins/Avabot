from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

CHROME = Service(executable_path="chromedriver.exe")
URL = "https://jumia.com.ng"


def search_items(items: list):        
    driver = webdriver.Chrome(service=CHROME)
    driver.get(URL)
    driver.implicitly_wait(10)
    html = driver.page_source
    time.sleep(20)

    driver.quit()

    soup = BeautifulSoup(html, "html5lib")
    print(soup.prettify())
