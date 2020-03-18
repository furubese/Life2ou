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

def status(server, num):
    if not server in {"sun", "moon", "mars", "earth"}:
        e = ["e", "Server Error"]
        return e
    
    url = "http://{}.chibiquest.net/staq2.php?num2={}".format(server, num)
    
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        e = ["e", e]
        return e
    except urllib.error.URLError as e:
        e = ["e", "メンテナンス中です。"]
        return e

    soup = BeautifulSoup(html, "html.parser")
    rs_price = soup.body.table.table.tr.td.td
    
    print(rs_price)

    return 0


def main(event,line_bot_api)
    #print(status("mars", "water01")[1])
    pass
