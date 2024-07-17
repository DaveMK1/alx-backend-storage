#!/usr/bin/env python3
"""
A module with tools for request caching and tracking
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """ Decorator for the get_page function
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper that:
            - verifies if the data for a URL is cached
            - counts the number of times get_page is invoked
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """ Sends an HTTP request to a specified endpoint
    """
    response = requests.get(url)
    return response.text
