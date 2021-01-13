import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://id.carousell.com/categories/tickets-and-voucher-18/events-and-tickets-687/?')
soup = BeautifulSoup(html_doc.text, 'html.parser')

tickets_terpopuler = soup.find(attrs={'class':'_2RJeLsMmpi'})

titles = tickets_terpopuler.findAll(attrs={'class':'TpQXuJG_eo'})

for title in titles:
    nama_produk = (title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
    image = (title.find('span',attrs={'class':'_3nH6adLACP _3k9K3fuPdS _14ECgRVNZW'}).find('img')['src'])
    print(image)

    with open('images/' + nama_produk + '.jpg','wb') as f:
        img = requests.get(image)
        f.write(img.content)
        