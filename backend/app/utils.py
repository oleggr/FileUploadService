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
            logger.alert(f'Config not found, check that file backend/config.py exist. Using default config.')
            return DefaultConfig()


class DefaultConfig:
    access_key = "some_access_key"
    secret_key = "some_secret_key"
    endpoint = "http://some-url.ru"
