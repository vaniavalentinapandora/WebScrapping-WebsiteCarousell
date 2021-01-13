import requests
import csv
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/kiyowoshop/reviews/')
soup = BeautifulSoup(html_doc.text, 'html.parser')

reviews = soup.find(attrs={'class':'_13w_InnkzD'})

titles = reviews.findAll(attrs={'class':'_1hkYwIYLT6'})

file = open('hasilreview.csv','w', newline='')
writer = csv.writer(file)
headers = ['Username','Review']
writer.writerow(headers)

for title in titles:
    reviews = title.find('p',attrs={'class':'_1gJzwc_bJS _2NNa9Zomqk Rmplp6XJNu mT74Grr7MA _2m1WFlGyTw lqg5eVwdBz _19l6iUes6V _3vlPf4XcxN _3k5LISAlf6'}).text
    username = title.find('span',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _1avuYeUOLe _3k5LISAlf6'}).text

    file = open('hasilreview.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([username, reviews])
file.close()