from diskcache import Cache
from slugify import slugify


class CacheHandler:
    """Cache Handle Class to get, generate and manipulate cache, the cache is save on ROOT/.cache
    using SQLite on background, the directory can changed setting the param on construct.
    ."""
    __instance = None
    cache = Cache(directory="./.cache")

    def __init__(self):
        if CacheHandler.__instance is not None:
            pass
            # raise Exception(MessageDefines.ERROR_SING)
        else:
            CacheHandler.__instance = self

    def set(self, key, value, expire=1440):
        """Set the key, value and time to expire in minutes

        :param key: String value to represent the cache name
        :param value: Value to the cache name 'key'
        :param expire: Time in minutes to expire cache
        :return: None
        """
        self.cache.set(key, value, expire)

    def get(self, key, default=None):
        """Return the value from key string

        :param key: String value to represent the cache name
        :param default: Value default if not existe key name yet
        :return: String with value from key name
        """
        return self.cache.get(key, default)

    def clear(self):
        """Clear all cache
        """
        self.cache.clear()

    @staticmethod
    def get_instance():
        if CacheHandler.__instance is None:
            CacheHandler()

        return CacheHandler.__instance

    def close(self):
        self.cache.close()


def cache_method(func):
    def custom_cache(*args, **kw):
        CacheHandler.get_instance()
        cache = CacheHandler()
        cache_name = func.__qualname__

        for var in args:
            if isinstance(var, str):
                if not ('database_manager_multibase' in var):
                    if not isinstance(var, list):
                        cache_name += "-" + var

        for k in sorted(kw.keys()):
            if not 'conn' in k:
                if not isinstance(kw[k], list):
                    cache_name += f"-{kw[k]}"

        cache_name = slugify(cache_name)
        if cache.get(cache_name) is None:
            result = func(*args, **kw)
            cache.set(cache_name, result)

        cache.close()
        return cache.get(cache_name)

    return custom_cache
