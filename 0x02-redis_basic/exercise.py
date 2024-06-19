#!/usr/bin/env python3
'''Module defines `Cache` class '''
from typing import Union
import uuid
import redis


class Cache:
    '''Defines caching in redis'''
    def __init__(self) -> None:
        '''Initialize the instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, bytes, float]) -> str:
        '''generate a random key'''
        k = str(uuid.uuid4())
        try:
            self._redis.set(k, data)
            return k
        except Exception:
            return ''
