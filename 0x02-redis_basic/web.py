#!/usr/bin/env python3
'''Redis Module
'''
import redis
import requests
from datetime import timedelta


def get_page(url: str) -> str:
    '''Fetches the content of a URL, caching the response and monitoring the request
    '''
    if url is None or len(url.strip()) == 0:
        return ''
    redis_store = redis.Redis()
    res_key = 'result:{}'.format(url)
    req_key = 'count:{}'.format(url)
    result = redis_store.get(res_key)
    if result is not None:
        redis_store.incr(req_key)
        return result
    result = requests.get(url).content.decode('utf-8')
    redis_store.setex(res_key, timedelta(seconds=10), result)
    return result
