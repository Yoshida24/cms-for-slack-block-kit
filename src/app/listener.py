from slack_bolt import App
from cms import MessageDef, ActionDef
import re

# "bot_message" サブタイプのメッセージを抽出するリスナーミドルウェア
def no_bot_messages(message, next):
    subtype = message.get("subtype")
    if subtype != "bot_message":
       next()

def listen_message(app: App, message_defs: list[MessageDef]):
    @app.event(event="message", middleware=[no_bot_messages])
    def message_handler(message, say):
        for message_def in message_defs:
            for trigger in message_def.triggers:
                if trigger.keyword in message["text"]:
                    say(
                        text="dummy",
                        blocks=message_def.blocks
                    )


def listen_action(app: App, action_defs: list[ActionDef]):
    @app.action(re.compile(""))
    def action_handler(body, ack, say):
        for action_def in action_defs:
            action_id = body["actions"][0]["action_id"]
            if action_id == action_def.id:
                value = body["actions"][0]["selected_option"]["value"] # value-N
                say(action_def.text + value)
                ack()