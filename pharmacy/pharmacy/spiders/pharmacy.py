import scrapy
import csv

class PharmacySpider(scrapy.Spider):
    name = "pharmacy"
    data = []
    with open("email.csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name','email'])

    with open('urls.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    start_urls = []
    for sublist in data:
        for item in sublist:
            start_urls.append(item)

    def parse(self, response):
        email = ""
        name = response.css('h1::text').get()
        main_info = response.css("table.data_table")
        if main_info is None:
            return
        main_details = main_info.css('tr')
        for th in main_details:
            if th and th.css('th::text').get()=='Email:':
                td = th.css('td')
                if td and td.css('p'):
                    email = td.css('p::text').get()
        if email != "":
            data = [name.strip(),email]
            with open('email.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)
