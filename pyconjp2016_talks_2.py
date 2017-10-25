import requests
from bs4 import BeautifulSoup

result = requests.get('http://pycon.jp/2016/ja/schedule/talks/list/')
#print(result.text)
soup = BeautifulSoup(result.text, 'html.parser')
