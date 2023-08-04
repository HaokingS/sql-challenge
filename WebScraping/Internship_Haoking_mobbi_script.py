from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
from fake_useragent import UserAgent
from lxml import etree
from bs4 import BeautifulSoup

user_agent = UserAgent()
options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument(f'user-agent={user_agent.random}')
# options.add_argument('--incognito')

# Function to get element
def getData(element):
    data = {}
    data['Product Link'] = 'https://www.mobbi.id' + element.find(".//a").get('href')
    data['Product Brand'] = element.get('data-product-brand')
    data['Product Model'] = element.get('data-product-category')
    data['Product Variant'] = element.get('data-product-variant')
    data['Product Price'] = element.get('data-product-price')
    data['Product Transmission'] = element.get('data-product-transmission')
    data['Product Mileage'] = element.get('data-product-mileage')
    data['Product Year'] = element.get('data-product-year')
    data['Product Location'] = element.get('data-product-location')
    return data

# Set up WebDriver and other variables
options = Options()
base_url = 'https://www.mobbi.id/'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(base_url)
time.sleep(5)
data = list()

driver.find_element("xpath", '//*[@id="btnwClear"]').click()
for i in range(1,3):
    driver.find_element("xpath", '//*[@id="headerNonIbid"]/li/div/div/form/div/div[1]/input[1]').click()
    driver.find_element("xpath", f'//*[@id="list-brand-search"]/li[{i}]').click()
    # Scrolling and Extract Data
    SCROLL_PAUSE_TIME = 3

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html_content = driver.page_source
    
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)
    elements = tree.xpath('//div[@class="featured-car-product for-compare-button no-rounded-bottom"]')
    data_list = [getData(element) for element in elements]
    data.extend(data_list)
driver.quit()
data = pd.DataFrame(data)

# Cleaning Data
data = data[data['Product Brand'].notna()] # Drop None
data['Product Price'] = data['Product Price'].dropna().apply(lambda x: int(float(x))) # Change Price Scientific Number to int
data['Product Mileage'] = data['Product Mileage'].astype(int) # Change Product Mileage to int

# Export to database
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
# variable environment
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE")

engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}')
connection = engine.connect()

table_name = 'Internship_Haoking_mobbi_scraping'
data.to_sql(table_name, engine, if_exists='replace', index=False)

# Export to CSV
data.to_csv('Internship_Haoking_mobbi_data.csv', index=False)