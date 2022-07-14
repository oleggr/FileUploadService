import importlib

from app.logger import logger


class ConfigLoader:
    config_name: str = 'config'

    @staticmethod
    def get_config():
        try:
            config = importlib.import_module(f'{ConfigLoader.config_name}')
            return config
        except ModuleNotFoundError as e:
            logger.alert(f'Config not found, check that file backend/config.py exist')
