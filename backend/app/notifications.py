import os
from abc import ABCMeta, abstractmethod

from app.utils import ConfigLoader


class notificator:
    @staticmethod
    def notify(message: str):
        TelegramNotificator().sendMessage(message)


class AbstractNotificator:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.config = ConfigLoader.get_config()

    @abstractmethod
    def sendMessage(self, message: str):
        """Send notification message.

        Used in mail and telegram notifications.

        @param message Notification message.
        """
        pass


class TelegramNotificator(AbstractNotificator):
    max_connection_time = 1
    tg_api_url = 'https://api.telegram.org/bot%s/sendMessage'

    def sendMessage(self, message: str):
        """Send notification message to telegram."""
        command = self.buildCommand(message)
        print("\n\n\n")
        print(command)
        print("\n\n\n")
        os.system(command)

    def buildUrl(self):
        """Build telegram api url to send notification message."""
        return self.tg_api_url % self.config.MONITORING_BOT_TOKEN

    def buildCommand(self, message):
        """Build curl cli command to send message to telegram notification bot."""
        return f'curl -s -X POST {self.buildUrl()} ' \
               f'--max-time {self.max_connection_time} ' \
               f'-d chat_id={self.config.NOTIFICATION_CHAT_ID}  ' \
               f'-d text=\"{message}\"'


class MailNotificator(AbstractNotificator):
    def sendMessage(self, message: str):
        pass
