from app.cache import RedisCache
from app.logger import logger
from app.notifications import notificator


if __name__ == '__main__':
    cache = RedisCache()

    keys_data = cache.get_all_keys()
    for key in keys_data:
        # if record ttl grater than 2 minutes then skip record
        if cache.DEFAULT_EXPIRE_TIME - keys_data[key] > 120:
            continue

        logger.info(f'Cache expired for key {key}')
        files = cache.get(key)
        if files:
            if notificator.send_success_email(key, files):
                cache.drop(key)
