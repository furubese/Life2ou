#!/usr/bin/env python
from flask import Flask, request, abort, render_template

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


def buttons_message(event, line_bot_api):
    profile = line_bot_api.get_profile(event.source.user_id)
    buttons_template_massage = TemplateSendMessage(
        alt_text='ボタンテンプレート',
        template=ButtonsTemplate(
            thumbnail_image_url=profile.picture_url,
            title=profile.display_name,
            text='選択せよ',
            actions=[
                PostbackAction(
                    label='postback',
                    display_text=f"User Id: {profile.user_id[:5]}...\n",
                    data='action = buy&itemid = 1'
                ),
                MessageAction(
                    label='message',
                    text='ここにメッセージが入る'
                ),
                URIAction(
                    label='uri',
                    uri='https://testcqlinehello.herokuapp.com/hello_page'
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token, buttons_template_massage
    )

def main(event, line_bot_api):
    buttons_message(event, line_bot_api)