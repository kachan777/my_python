import requests

result = requests.get('http://pycon.jp/2016/ja/schedule/talks/list/')
print(result.text)
