from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
# options.add_argument('--headless') #ウェブを表示しない
#勝手にブラウザを閉じない
options.add_experimental_option('detach', True)

# ウェブブラウザの起動
browser = webdriver.Chrome(options=options)

url='https://scraping-for-beginner.herokuapp.com/login_page'
browser.get(url)
username = browser.find_element(By.ID, "username")
username.send_keys('imanishi')

password = browser.find_element(By.ID, "password")
password.send_keys('kohei')

loginButton = browser.find_element(By.ID, "login-btn")
loginButton.click()

elem = browser.find_element(By.ID, "name")
print(elem.text)


keys = []
elems_th = browser.find_elements(By.TAG_NAME, "th")
for elem_th in elems_th:
  keys.append(elem_th.text)
print(keys)

values = []
elems_td = browser.find_elements(By.TAG_NAME, "td")
for elem_td in elems_td:
  values.append(elem_td.text)
print(values)

# 空のテーブル作成
df = pd.DataFrame()
df['項目']= keys
df['値'] = values
df.to_csv('講師情報.csv', index=False)


# ウェブブラウザを閉じる
browser.quit()


