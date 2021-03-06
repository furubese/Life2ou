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
        alt_text='デフォルトボタン',
        template=ButtonsTemplate(
            thumbnail_image_url=profile.picture_url,
            title=profile.display_name,
            text='こんにつは！',
            actions=[
                PostbackAction(
                    label='User',
                    display_text=f"User Id: {profile.user_id}...",
                    data='action = buy&itemid = 1'
                ),
                MessageAction(
                    label='ソース',
                    text='https://github.com/furubese/Life2ou/tree/master/Life2ou\n'\
                         '【MODS】\n'\
                         'https://github.com/furubese/Life2ou/tree/master/Life2ou/mod'
                ),
                URIAction(
                    label='これのソースURL',
                    uri='https://github.com/furubese/Life2ou/blob/master/Life2ou/mod/button_message.py'
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token, buttons_template_massage
    )

def main(event, line_bot_api):
    buttons_message(event, line_bot_api)
