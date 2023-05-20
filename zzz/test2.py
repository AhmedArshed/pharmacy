import csv



data = []


with open('urls.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)
    start_urls = []
    for sublist in data:
        for item in sublist:
            start_urls.append(item)

# print(len(start_urls))