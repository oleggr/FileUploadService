import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.utils import ConfigLoader


class notificator:
    @staticmethod
    def notify(message: str):
        TelegramNotificator().sendMessage(message)

    @staticmethod
    def send_email(request_id: str, files: list):
        MailNotificator().sendMessage(request_id, files)


class TelegramNotificator:
    max_connection_time = 1
    tg_api_url = 'https://api.telegram.org/bot%s/sendMessage'

    def __init__(self):
        self.config = ConfigLoader.get_config()

    def sendMessage(self, message: str):
        """Send notification message to telegram."""
        command = self.buildCommand(message)
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


class MailNotificator:
    def __init__(self):
        self.config = ConfigLoader.get_config()

    def sendMessage(self, request_id: str, files: list):
        mail = MIMEMultipart()
        mail['Subject'] = f"В заявку №{request_id} добавлены файлы"

        files_str = ''
        for file in files:
            files_str += file + "\n"
        mail_content = f"В заявку №{request_id} добавлены файлы:\n{files_str}"
        mail.attach(MIMEText(mail_content, 'plain'))

        with smtplib.SMTP(
                self.config.MAIL_SMTP_SERVER,
                self.config.MAIL_PORT
        ) as server:
            for receiver in self.config.MAIL_RECEIVERS:
                mail['From'] = self.config.MAIL_SENDER
                mail['To'] = receiver

                server.sendmail(
                    self.config.MAIL_SENDER,
                    receiver,
                    mail.as_string()
                )
