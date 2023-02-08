import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url) #レスポンス
soup = BeautifulSoup(res.text, 'html.parser')
img_tags = soup.find_all('img')



for i, img_tag in enumerate(img_tags):
  img_tag['src']

  root_url = 'https://scraping-for-beginner.herokuapp.com'
  img_url = root_url + img_tag['src']

  # 文字列データをバイナリデータに変換
  img_bin = io.BytesIO(requests.get(img_url).content)
  #バイナリデータをPillowで開く
  img = Image.open(img_bin)
  #ファイル名を付けて保存
  img.save(f'img/{i}.jpg')
