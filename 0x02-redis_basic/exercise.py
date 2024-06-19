#!/usr/bin/env python3
'''Module defines `Cache` class '''
import redis
import uuid
from typing import Union


class Cache:
    '''Defines caching in redis'''
    def __init__(self):
        '''Initialize the instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, bytes, float]) -> str:
        '''generate a random key'''
        k = str(uuid.uuid4())
        self._redis.set(k, data)
        return k
