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
    msg += str(i + 1) + '. ' + data[1] + ' (' + str(data[0]) + ')\n'
  return msg

# 最新のコンテストの成績を取得
def getResultList():
    list = []
    late = '2019-12-29T21:40:00+09:00'
    for user in users['ac']:
        data = json.loads(requests.get(url.format(name=user)).text)
        data[-1]['name'] = user
        if late == data[-1]['EndTime']:
            list.append(data[-1])
        elif late < data[-1]['EndTime']:
            list = []
            list.append(data[-1])
            late = data[-1]['EndTime']
    list.sort(key=lambda x: x['Place'])
    return list

# 1. oevl(598)
# perf: 1583 rating: 1427 -> 1444 (+17)
def makeResultMsg(list):
    msg = '「' + list[-1]['ContestName'] + ' の成績です！」\n'
    for i, data in enumerate(list):
        dif = str(data['NewRating'] - data['OldRating'])
        if dif > '0':
            dif = '+' + dif
        msg += str(i + 1) + '. ' + data['name']
        msg += '(' + str(data['Place']) + ')\n'
        msg += 'perf: ' + str(data['Performance']) + '\n'
        msg += 'rating: ' + str(data['OldRating']) + ' -> ' + str(data['NewRating']) + ' (' + dif + ')\n'
    return msg


# 以下はbotが直接呼び出す関数
def getAC():
  return makeMsg(getACList())

def getRating():
  return makeMsg(getRatingList())

def getCFRating():
  return makeMsg(getCFRatingList())

def getResult():
    return makeResultMsg(getResultList())



# デバッグ用
# print(getAC())
# print(getRating())
# print(getCFRating())





# {'name': 'oevl', 'Performance': 1583, 'ContestName': 'AtCoder Beginner Contest 152', 'InnerPerformance': 1583, 'ContestNameEn': '', 'EndTime': '2020-01-19T22:30:00+09:00', 'OldRating': 1427, 'NewRating': 1444, 'IsRated': True, 'ContestScreenName': 'abc152.contest.atcoder.jp', 'Place': 598}

# 最新回のパフォーマンスを取得
# url = 'https://atcoder.jp/users/{name}/history/json'
def getAllInfo():
  list = []
  for user in users['ac']:
    data = json.loads(requests.get(url.format(name=user)).text)
    list.append([data[-1]['Performance'], user])
  return list

print(makeResultMsg(getResultList()))
# list = getAllInfo()
# print(list)
