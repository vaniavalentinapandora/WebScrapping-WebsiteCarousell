import requests
import csv
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/categories/health-and-beauty-11/makeup-309/?')
soup = BeautifulSoup(html_doc.text, 'html.parser')

makeup_terpopuler = soup.find(attrs={'class':'_2RJeLsMmpi'})

titles = makeup_terpopuler.findAll(attrs={'class':'TpQXuJG_eo'})

file = open('hasilextraction.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Nama Toko', 'Nama Produk', 'Harga']
writer.writerow(headers)

for title in titles:
    toko = (title.find('p',attrs={'class':'_1gJzwc_bJS _2NNa9Zomqk Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
    nama = (title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
    harga =(title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}).text)

    file = open('hasilextraction.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([toko, nama, harga])
    file.close()