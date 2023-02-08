import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url) #レスポンス

# htmlの塊の構造を正す(soup.prettify()でインデント付)
soup = BeautifulSoup(res.text, 'html.parser')

data = []

#一つの観光地情報を取得(div群の最初の要素)
spots = soup.find_all('div', attrs={'class': 'u_areaListRankingBox'})
for spot in spots:
  spotName = spot.find('div', attrs={'class': 'u_title'})
  # 特定要素を削除する + いらない文字列を削除する
  spotName.find('span', attrs={'class': 'badge'}).extract()
  spotNameText = spotName.text.replace('\n', '')

  #　点数
  spotPoints= float(spot.find('div', attrs={'class': 'u_rankBox'}).text)

  # 観光地の点数における各要素
  categoryByItems= spot.find('div', attrs={'class': 'u_categoryTipsItem'})
  categoryByItems = categoryByItems.find_all('dl')

  details = {}
  for categoryItem in categoryByItems:
    category = categoryItem.dt.text
    rank = float(categoryItem.span.text)
    details[category] = rank
  # {'楽しさ': 4.6, '人混みの多さ': 4.5, '景色': 4.9, 'アクセス': 4.2}

  datum = details
  datum['観光地名'] = spotNameText
  datum['評価点'] = spotPoints
  data.append(datum)
  print(datum)
print(data)

# dataを入れた上でテーブル作成
df = pd.DataFrame(data)
df = df[['観光地名', '評価点', '楽しさ', '人混みの多さ', '景色', 'アクセス']]
print(df)
df.to_csv('観光名所.csv', index=False)
