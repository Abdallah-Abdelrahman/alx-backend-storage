#!/usr/bin/env python3
'''Module defines `Cache` class '''
from typing import Callable, Union
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
        if isinstance(data, (int, str, bytes, float)):
            self._redis.set(k, data)
            return k
        return ''

    def get(self, key: str, fn: Callable = lambda x: x) -> Union[str, int]:
        '''convert the data back to the desired format'''
        return fn(key)

    def get_str(self, key: str) -> str:
        '''paramertize `get` with str convertor'''
        return self.get(key, fn=lambda x: x.decode('utf8'))

    def get_int(self, key: str) -> int:
        '''parameterize `` with int convertor '''
        return self.get(key, fn=lambda x: int(x))
