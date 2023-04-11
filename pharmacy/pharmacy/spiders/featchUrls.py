
import requests
import traceback
import csv
from bs4 import BeautifulSoup


def get_url():
    try:
        url = 'https://www.e-vuc.sk/sitemap.html'
        page = requests.get(url)
        if page.status_code != 200:
            print("check issue")
        sitemap_index = BeautifulSoup(page.content, 'html.parser')
        sitemap_url = [
            element.text for element in sitemap_index.findAll('loc')]
        with open('urls.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sitemap_url)
    except Exception as e:
        message = "Error: " + str(e) + "\n" + traceback.format_exc()
        print(message)

get_url()