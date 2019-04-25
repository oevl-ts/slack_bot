import requests
import json

api = 'https://kenkoooo.com/atcoder/atcoder-api/v2/user_info?user='
api_cf = 'https://codeforces.com/api/user.info?handles='
url = 'https://atcoder.jp/users/{name}/history/json'

# ユーザ名の読み込み
with open('./users.json') as u:
  users = json.load(u)

# AtCoderのAC数を取得
def getACList():
  list = []
  for user in users['ac']:
    data = json.loads(requests.get(api + user).text)
    list.append([data['accepted_count'], user])
  return list

# AtCoderのレートを取得
def getRatingList():
  list = []
  for user in users['ac']:
    data = json.loads(requests.get(url.format(name=user)).text)
    list.append([data[-1]['NewRating'], user])
  return list

# こどふぉのレートを取得
def getCFRatingList():
  list = []
  for user in users['cf']:
    data = json.loads(requests.get(api_cf + user).text)
    list.append([data['result'][0]['rating'], user])
  return list

# 送信するメッセージを作成
def makeMsg(list):
  msg = ''
  list.sort(reverse = True)
  for i, data in enumerate(list):
    msg += str(i + 1) + ' : ' + data[1] + ' : ' + str(data[0]) + '\n'
  return msg

# 以下はbotが直接呼び出す関数
def getAC():
  return makeMsg(getACList())

def getRating():
  return makeMsg(getRatingList())

def getCFRating():
  return makeMsg(getCFRatingList())

# デバッグ用
# print(getAC())
# print(getRating())
# print(getCFRating())
