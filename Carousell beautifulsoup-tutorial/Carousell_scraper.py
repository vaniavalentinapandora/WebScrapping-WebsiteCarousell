import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/categories/photography-6/')
soup = BeautifulSoup(html_doc.text, 'html.parser')

kamera_terpopuler = soup.find(attrs={'class':'_2RJeLsMmpi'})

titles = kamera_terpopuler.findAll(attrs={'class':'TpQXuJG_eo'})

for title in titles:

    #nama toko
    print(title.find('p',attrs={'class':'_1gJzwc_bJS _2NNa9Zomqk Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)

    # deskripsi barang
    print(title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv'}).text)

    # nama title
    print(title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)

    # Image
    print(title.find('div',attrs={'class':'_3nH6adLACP _3k9K3fuPdS _14ECgRVNZW'}).find('img')['src'])

    # Harga
    print(title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}).text)
