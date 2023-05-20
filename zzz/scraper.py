import requests
import csv
from bs4 import BeautifulSoup

data = []
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email', 'Phone', 'Address', 'Website'])

with open('urls.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
    start_urls = []
    for sublist in data:
        for url in sublist:
            response = requests.get(url)

            # Create a BeautifulSoup object from the HTML content
            soup = BeautifulSoup(response.content, "html.parser")
            contact_div = soup.find('div', {'class': 'lower-box clearfix mt-2'})

            # Extract the email, phone number, mobile, address, and website from the div
            email = contact_div.find('span', {'itemprop': 'email'}).text.split()[0] if contact_div.find('span', {'itemprop': 'email'}) else None
            phone = contact_div.find('span', {'itemprop': 'telephone'}).text.strip() if contact_div.find('span', {'itemprop': 'telephone'}) else None
            mobile = contact_div.find('span', {'itemprop': 'telephone'}).text.strip() if contact_div.find('span', {'itemprop': 'telephone'}) else None
            address = contact_div.find('span', {'itemprop': 'streetAddress'}).text.strip() if contact_div.find('span', {'itemprop': 'streetAddress'}) else None
            website = contact_div.find('span', {'itemprop': 'sameAs'}).text.strip() if contact_div.find('span', {'itemprop': 'sameAs'}) else None

            # Print the extracted data
            with open('data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([email,phone,address,website])