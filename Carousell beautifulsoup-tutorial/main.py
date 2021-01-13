import bs4
import requests

url = 'https://id.carousell.com/carousell_id/'
contents = requests.get(url)
# print(contents)
print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")
# print(response)
data = response.find_all('div', '_2aXUJrQ50K _1rq1uz_KQ6 _3hkhiFRFl8')
print(data[0].text)