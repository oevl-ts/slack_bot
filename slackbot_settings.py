import os

# botアカウントのトークンを指定
# 環境変数に"token"を設定
API_TOKEN = os.environ['token']

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "「AC」または「レート」を含むメッセージを送信してください"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
