import requests
from bs4 import BeautifulSoup

url = "https://scraping-for-beginner.herokuapp.com/udemy"
res = requests.get(url) #レスポンス

# htmlの塊の構造を正す(soup.prettify()でインデント付)
soup = BeautifulSoup(res.text, 'html.parser')

# タグとクラスから要素取得　+ テキスト化し数値抽出
subscribers = soup.find_all('p', attrs={'class': 'subscribers'})[0]
n_subscribers =int(subscribers.text.split("：")[1])
print(n_subscribers)

# 上記をCSSセレクタで取得
subscribers2 = soup.select_one('.subscribers')
n_subscribers2 =int(subscribers2.text.split("：")[1])
print(n_subscribers2)


reviews = soup.find_all('p', attrs={'class': 'reviews'})[0]
n_reviews = int(reviews.text.split("：")[1])
print(n_reviews)