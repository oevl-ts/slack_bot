from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import get_info as gi

@respond_to(r'AC')
def mention_func(message):
    message.reply(gi.getAC())
    message.react('+1')

@respond_to(r'レート')
def mention_func(message):
    message.reply(gi.getRate())
    message.react('smiley')

@respond_to(r'ソースコード')
def mention_func(message):
    message.reply('「ソースコードです！」')
    message.reply('https://github.com/oevlreyo/slack_bot')
    message.react('sunglasses')
