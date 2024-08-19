# -*- coding: utf-8 -*-
http://192.168.100.129:5555/random

import requests

PROXY_POOL_URL = 'http://192.168.100.129:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
