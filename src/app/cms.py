from dataclasses import dataclass

@dataclass
class MessageTrigger():
    handler_id: str
    keyword: str


@dataclass
class MessageDef():
    id: str
    blocks: list[dict]
    triggers: list[MessageTrigger]


def message_definitions() -> list[MessageDef]:
    return [
        MessageDef(
            id="message_1",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hello there!"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text":"Click Me 1"},
                        "action_id": "button_click_1"
                    }
                }
            ],
            triggers=[
                MessageTrigger(
                    handler_id='message_1',
                    keyword='hello'
                )
            ]
        ),
        MessageDef(
            id="message_2",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hi there!"
                    },
                    "accessory": {
                        "type": "button",
                        "text": {"type": "plain_text", "text":"Click Me 2"},
                        "action_id": "button_click_2"
                    }
                }
            ],
            triggers=[
                MessageTrigger(
                    handler_id='message_2',
                    keyword='hi'
                )
            ]
        )
    ]


@dataclass
class ActionTrigger():
    handler_id: str
    keyword: str


@dataclass
class ActionDef():
    id: str
    text: str


def action_definitions() -> list[ActionDef]:
    return [
        ActionDef(
            id="button_click_1",
            text="<@U04TUT8RC3T> clicked the button 1"
        ),
        ActionDef(
            id="button_click_2",
            text="<@U04TUT8RC3T> clicked the button 2"
        )
    ]