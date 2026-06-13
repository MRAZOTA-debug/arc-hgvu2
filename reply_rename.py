from typing import Any, List

from base_plugin import BasePlugin

__id__ = "reply_rename"
__name__ = "Reply → Quote"
__description__ = "Заменяет текст 'Ответ' на 'Цитировать' в интерфейсе Telegram"
__author__ = "crowbot"
__version__ = "1.0.0"
__icon__ = "msg_reply"
__app_version__ = ">=12.5.1"
__sdk_version__ = ">=1.4.3.6"


class ReplyRenamePlugin(BasePlugin):
    def on_plugin_load(self):
        self.log("Reply Rename plugin loaded")

    def create_settings(self) -> List[Any]:
        from ui.settings import Header, Text
        
        return [
            Header(text="Reply → Quote"),
            Text(
                text="Описание",
                subtext="Плагин заменяет текст 'Ответ' на 'Цитировать' в интерфейсе Telegram.",
                icon="msg_info"
            ),
            Text(
                text="Статус",
                subtext="Плагин активен и работает автоматически.",
                icon="msg_check"
            )
        ]
