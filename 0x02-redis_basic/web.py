#!/usr/bin/env python3
'''Module defines `get_page` function'''
from typing import Callable
import requests
import redis
from functools import wraps

# Initialize Redis client
local_redis = redis.Redis()


def cache_result(fn):
    '''Decorator to cache the result of a function,
    for a given expiration time.
    '''
    @wraps(fn)
    def wrapper(url: str) -> str:
        '''The real wrapper'''
        # Check if the result is in cache
        k = 'count:{}'.format(url)
        cached_result = local_redis.get(k)
        if cached_result:
            return cached_result.decode('utf8')

        # Call the function and get the result
        result = fn(url)

        # Cache the result with the expiry of 10 seconds
        local_redis.setex(k, 10000, result)
        return result
    return wrapper


def track_access_count(fn: Callable) -> Callable:
    '''Decorator to track how many times a URL was accessed.'''
    @wraps(fn)
    def wrapper(url: str) -> str:
        '''wrapper function to increment count'''
        # Increment the access count for the URL
        k = f'count:{url}'
        if not local_redis.get(k):
            local_redis.set(k, 1)
        else:
            local_redis.incr(k)
        return fn(url)
    return wrapper


@cache_result
@track_access_count
def get_page(url: str) -> str:
    '''Fetch the HTML content of a URL and return it.'''
    response = requests.get(url)
    return response.text
