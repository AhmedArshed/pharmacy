import scrapy
import csv

class PharmacySpider(scrapy.Spider):
    name = "pharmacy"
    data = []
    with open('details.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Email', 'Phone', 'Address', 'Website'])

    with open('urls.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    start_urls = []
    for sublist in data:
        for item in sublist:
            start_urls.append(item)
    def parse(self, response):
        contact_div = response.css('div.lower-box.clearfix.mt-2')

        email = contact_div.css('span[itemprop="email"]::text').get(default=None)
        if email is not None:
            email = email.split()[0]

        phone = contact_div.css('span[itemprop="telephone"]::text').get(default=None)
        mobile = phone

        address = contact_div.css('span[itemprop="streetAddress"]::text').get(default=None)
        website = contact_div.css('span[itemprop="sameAs"]::text').get(default=None)

        with open('details.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email,phone,address,website])
