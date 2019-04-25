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
  list.sort(reverse = True)
  return list

# AtCoderのレートを取得
def getRatingList():
  list = []
  for user in users['ac']:
    data = json.loads(requests.get(url.format(name=user)).text)
    list.append([data[-1]['NewRating'], user])
  list.sort(reverse = True)
  return list

# こどふぉのレートを取得
def getCFRatingList():
  list = []
  for user in users['cf']:
    data = json.loads(requests.get(api_cf + user).text)
    list.append([data['result'][0]['rating'], user])
    list.sort(reverse = True)
  return list

# リストから送信するメッセージを作成
def makeMsg(list):
  msg = ''
  for i, data in enumerate(list):
    msg += str(i + 1) + ' : '
    msg += data[1] + ' : '
    msg += str(data[0]) + '\n'
  return msg

# 以下はbotが呼び出す関数
def getAC():
  list = getACList()
  msg = makeMsg(list)
  return msg

def getRating():
  list = getRatingList()
  msg = makeMsg(list)
  return msg

def getCFRating():
  list = getCFRatingList()
  msg = makeMsg(list)
  return msg


# デバッグ用
# print(getAC())
# print(getRating())
# print(getCFRating())

def getInfo():
  for user in users['user']:
    data = json.loads(requests.get(url.format(name=user)).text)
    print(data[-1])
  for user in users['user']:
    data = json.loads(requests.get(api + user).text)
    print(data)
# getInfo()
