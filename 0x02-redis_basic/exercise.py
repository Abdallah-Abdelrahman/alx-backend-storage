#!/usr/bin/env python3
'''Module defines `Cache` class '''
from typing import Any, Callable, Union
import uuid
import redis
from functools import wraps


def call_history(method: Callable) -> Callable:
    '''decorator that returns wrapper function.
    it stores history of inputs and outputs
    '''
    @wraps(method)
    def decorate(self, *args, **kw):
        '''The real decorator'''
        input_key = method.__qualname__ + ':inputs'
        output_key = method.__qualname__ + ':outputs'

        # Store the input arguments
        self._redis.rpush(input_key, str(args))

        # Execute the original function and get the output
        result = method(self, *args, **kw)

        # Store the output
        self._redis.rpush(output_key, str(result))

        return result
    return decorate


def count_calls(method: Callable) -> Callable:
    '''decorator that returns wrapper function.
    it counts how many times it's called for a key
    '''
    @wraps(method)
    def decorate(self, *args, **kw):
        '''The real decorator'''
        if not self.get(method.__qualname__):
            self._redis.set(method.__qualname__, 1)
        else:
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kw)
    return decorate


class Cache:
    '''Defines caching in redis'''
    def __init__(self) -> None:
        '''Initialize the instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[int, str, bytes, float]) -> str:
        '''generate a random key'''
        k = str(uuid.uuid4())
        if isinstance(data, (int, str, bytes, float)):
            self._redis.set(k, data)
            return k
        return ''

    def get(self,
            key: str,
            fn: Callable = lambda x: x) -> Any:
        '''convert the data back to the desired format'''
        data = self._redis.get(key)

        if data is None:
            return data
        if fn:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        '''paramertize `get` with str convertor'''
        return self.get(key, fn=lambda x: x.decode('utf8'))

    def get_int(self, key: str) -> int:
        '''parameterize `` with int convertor '''
        return self.get(key, fn=lambda x: int(x))


def replay(method: Callable) -> None:
    '''Display the history of calls of a particular function'''
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    input_key = f'{method_name}:inputs'
    output_key = f'{method_name}:outputs'

    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    call_count = len(inputs)

    print(f'{method_name} was called {call_count} times:')

    for input_val, output_val in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(method_name,
                                     input_val.decode('utf-8'),
                                     output_val.decode('utf-8')))
