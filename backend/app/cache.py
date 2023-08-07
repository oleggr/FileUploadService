from redis import ConnectionPool, Redis
import pickle

from app.logger import logger
from app.utils import ConfigLoader


class RedisCache:
    master: Redis
    DEFAULT_EXPIRE_TIME = 3600  # in seconds (1 hour)

    def __init__(self):
        config = ConfigLoader.get_config()
        pool = ConnectionPool(
            host=config.redis_host,
            port=config.redis_port,
            db=0,
            password=config.redis_password
        )
        self.master = Redis(connection_pool=pool)

    def set(self, request_id: str, filename: str):
        files = self.get(request_id)
        if not files:
            raise Exception('Something went wrong while reading redis record')

        files.append(filename)

        # self.master.ttl()

        try:
            logger.info(f'Set "{filename}" to Redis for request "{request_id}".')
            self.master.set(request_id, pickle.dumps(files), ex=self.DEFAULT_EXPIRE_TIME)
        except Exception as e:
            logger.alert(f'Error while setting "{filename}" to Redis for request "{request_id}": {e}')

    def get(self, request_id: str):
        record = None

        try:
            logger.info(f'Get record from Redis for request "{request_id}".')
            value = self.master.get(request_id)
            record = pickle.loads(value)
        except Exception as e:
            logger.alert(f'Error while getting record from Redis for request "{request_id}": {e}')

        return record if record else []

    def drop(self, request_id: str):
        try:
            logger.info(f'Delete record from Redis for request "{request_id}".')
            self.master.delete(request_id)
        except Exception as e:
            logger.alert(f'Error while deleting record from Redis for request "{request_id}": {e}')

    def get_all_keys(self):
        keys_data = {}

        try:
            logger.info(f'Get all keys from Redis".')
            keys = self.master.keys('*')
            for key in keys:
                keys_data[key] = self.master.ttl(key)
        except Exception as e:
            logger.alert(f'Error while getting all files from Redis: {e}')

        return keys_data
