import importlib
def replay_message(event, line_bot_api):

    base = "pack.Life2ou.mod"
    module = {
        "うんち": "rp_unchi",
        "ボタンの表示": "button_message",
        "検索=": "energy",
        "水のステータス見せて": "cq_status"
        }

    for m in module:
        if m in event.message.text:
            importlib.import_module(base + "." + module[m]).main(event, line_bot_api)
