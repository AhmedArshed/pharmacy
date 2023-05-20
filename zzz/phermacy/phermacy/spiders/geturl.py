from selenium import webdriver
from bs4 import BeautifulSoup
from scrapy import Selector
import csv

url = 'https://www.zzz.sk/zariadenia/slovensko/'

# Set up a headless Chrome browser instance
all_urls = []
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(options=options)

# Load the page in the browser
driver = webdriver.Chrome( options=options)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

alg_selectors = soup.select('a.alg_selector')
for selector in alg_selectors:
    href = selector.get('href')
    all_urls.append("https://www.zzz.sk"+href)

for i in range(2, 801):
    new_url = url+"?page="+str(i)
    driver.get(new_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    alg_selectors = soup.select('a.alg_selector')
    for selector in alg_selectors:
        href = selector.get('href')
        all_urls.append("https://www.zzz.sk"+href)

unique_list = list(set(all_urls))
print(len(unique_list))
with open('urls.csv', mode='w', newline='') as file:
    writer = csv.writer(file,lineterminator='\n')
    writer.writerow(unique_list)
browser.quit()
