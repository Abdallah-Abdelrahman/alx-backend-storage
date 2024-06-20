#!/usr/bin/env python3
'''Module defines `get_page` function'''
from typing import Callable
import requests
import redis
from functools import wraps

# Initialize Redis client
local_redis = redis.Redis()


def cache_result(expiration: int = 1):
    '''Decorator to cache the result of a function,
    for a given expiration time.
    '''
    def decorator(func: Callable) -> Callable:
        '''inner wrapper'''
        @wraps(func)
        def wrapper(url: str) -> str:
            '''The real wrapper'''
            # Check if the result is in cache
            cached_result = local_redis.get(f"cache:{url}")
            if cached_result:
                return cached_result.decode('utf-8')

            # Call the function and get the result
            result = func(url)

            # Cache the result with the given expiration time
            local_redis.setex(f"cache:{url}", expiration, result)
            return result
        return wrapper
    return decorator


def track_access_count(func: Callable) -> Callable:
    '''Decorator to track how many times a URL was accessed.'''
    @wraps(func)
    def wrapper(url: str) -> str:
        '''wrapper function to increment count'''
        # Increment the access count for the URL
        local_redis.incr(f"count:{url}")
        return func(url)
    return wrapper


@cache_result(expiration=10)
@track_access_count
def get_page(url: str) -> str:
    '''Fetch the HTML content of a URL and return it.'''
    response = requests.get(url)
    return response.text
