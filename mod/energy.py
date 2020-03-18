#!/usr/bin/env python

"""
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
# ここにモジュール追加していく。
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate,
    MessageAction, URIAction, PostbackAction,

)
"""
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

def amazones_product(rs_price, rs_picture, i):
    price = rs_price[i].string
    name = rs_picture[i].get("alt")
    picture = rs_picture[i].get("src")

    mm = {
        "name": name,
        "price": price,
        "picture": picture
        }

    return mm
    

def amazones_serch(word, vol):
    serch = urllib.parse.quote(word)
    url = "https://www.amazon.co.jp/s?k={}".format(serch)
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        e = [e]
        return e

    soup = BeautifulSoup(html, "html.parser")
    rs_price= soup.select('span.a-offscreen')
    rs_picture= soup.select('img.s-image')

    product=[]
    for i in range(vol):
        product.append(amazones_product(rs_price, rs_picture, i))
    return product

def line_print(event, line_bot_api, message):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message)
        )

def amazones_atach(event, line_bot_api, word):
    vol = "3"
    try:
        vol = int(vol)
        if vol > 5:
            line_print(event, line_bot_api, "max=5")
    except ValueError as e:
        line_print(event, line_bot_api, e)
        
    res = amazones_serch(word, vol)
    if not len(res) > 1:
        line_print(event, line_bot_api, res[0])
        return 1
    ans = ""
    for i in range(vol):
        ans += res[i]["name"] + "\n" +\
              res[i]["price"] + "\n" +\
              res[i]["picture"]
        ans += "\n"
    ans = ans[:-1]
    
    line_print(event, line_bot_api, ans)
          

def main(event, line_bot_api):
    word = event.message.text.split('検索=')[1]
    amazones_atach(event, line_bot_api, word)
