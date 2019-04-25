from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import get_info as gi

@respond_to(r'AC')
def mention_func(message):
    message.reply('「AtCoder AC数ランキングです！」\n' + gi.getAC())
    message.react('+1')

@respond_to(r'レート')
def mention_func(message):
    message.reply('「AtCoder レートランキングです！」\n' + gi.getRating())
    message.react('smiley')

@respond_to(r'こどふぉ')
def mention_func(message):
    message.reply('「Codeforces レートランキングです！」\n' + gi.getCFRating())
    message.react('ru')

@respond_to(r'ソースコード')
def mention_func(message):
    message.reply('「ソースコードです！」\n' + 'https://github.com/oevlreyo/slack_bot')
    message.react('sunglasses')

@default_reply()
def default_func(message):
    message.reply("「レート」「AC」「こどふぉ」")
    message.react('pray')
