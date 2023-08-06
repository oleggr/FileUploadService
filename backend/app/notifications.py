import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.logger import logger
from app.utils import ConfigLoader

EMAIL_SEND_MAX_RETRIES = 10

class notificator:
    @staticmethod
    def notify(message: str):
        TelegramNotificator().sendMessage(message)

    @staticmethod
    def send_success_email(request_id: str, files: list):
        email_send_retries = 1

        while email_send_retries <= EMAIL_SEND_MAX_RETRIES:
            try:
                MailNotificator().successMessage(request_id, files)
                return
            except Exception as e:
                logger.alert(f'Failed send success email for request {request_id}: {e}.')
                email_send_retries += 1

        logger.alert(f'Retries exceeded for sending success email for request {request_id}')

    @staticmethod
    def send_failed_email(request_id: str, error: str):
        email_send_retries = 1

        while email_send_retries <= EMAIL_SEND_MAX_RETRIES:
            try:
                MailNotificator().failedMessage(request_id, error)
                return
            except Exception as e:
                logger.alert(f'Failed send fail email for request {request_id}: {e}.')
                email_send_retries += 1

        logger.alert(f'Retries exceeded for sending failed email for request {request_id}')


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

    def successMessage(self, request_id: str, files: list):
        mail_subject = f"В заявку [TicketID: {request_id}] добавлены  файлы"
        files_str = ''
        for file in files:
            files_str += file + "\n"
        mail_content = f"В заявку [TicketID: {request_id}] добавлены файлы:\n{files_str}"

        self.sendMessage(mail_subject, mail_content)

    def failedMessage(self, request_id: str, error: str):
        mail_subject = f"Ошибка добавления файлов к заявке №{request_id}"
        mail_content = f"Ошибка добавления файлов к заявке №{request_id}: {error}"

        self.sendMessage(mail_subject, mail_content)

    def sendMessage(self, mail_subject, mail_content):
        mail = MIMEMultipart()
        mail['Subject'] = mail_subject
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
