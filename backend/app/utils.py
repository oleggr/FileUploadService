import importlib

from app.logger import logger


class ConfigLoader:
    config_name: str = 'config'

    @staticmethod
    def get_config():
        try:
            config = importlib.import_module(ConfigLoader.config_name)
            return config
        except ModuleNotFoundError:
            logger.alert('Config not found, check that file backend/config.py exist. Using default config.')
            return DefaultConfig()


class DefaultConfig:
    access_key = "some_access_key"
    secret_key = "some_secret_key"
    endpoint = "http://some-url.ru"
    LOGS_FOLDER = 'logs/'
    MONITORING_BOT_TOKEN = "some_tg_token"
    NOTIFICATION_CHAT_ID = 123456789
    MAIL_PORT = 25
    MAIL_SMTP_SERVER = "127.0.0.1"
    MAIL_SENDER = ""
    MAIL_RECEIVERS = [""]
