import requests
import json

# Ploblems API
api = 'https://kenkoooo.com/atcoder/atcoder-api/v2/user_info?user='
url = 'https://atcoder.jp/users/{name}/history/json'

# ユーザ名の読み込み
with open('./users.json') as u:
  users = json.load(u)

# AC数を取得して、投稿するメッセージを作成
def getAC():
  # ユーザのAC数を取得
  list = []
  for user in users['user']:
    data = json.loads(requests.get(api + user).text)
    list.append([data['accepted_count'], user])

  # ソート
  list.sort(reverse = True)

  # メッセージを作成
  msg = '「AtCoder AC数ランキングです！」\n'
  for i, data in enumerate(list):
    msg += str(i + 1) + ' : '
    msg += data[1] + ' : '
    msg += str(data[0]) + '\n'
  return msg

# レートを取得して、投稿するメッセージを作成
def getRate():
  # ユーザのレートを取得
  list = []
  for user in users['user']:
    data = json.loads(requests.get(url.format(name=user)).text)
    list.append([data[-1]['NewRating'], user])

  # ソート
  list.sort(reverse = True)

  # 投稿するメッセージを作成
  msg = '「AtCoder レートランキングです！」\n'
  for i, data in enumerate(list):
    msg += str(i + 1) + ' : '
    msg += data[1] + ' : '
    msg += str(data[0]) + '\n'
  return msg

print(getAC())
print(getRate())
