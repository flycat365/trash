# -*- coding: utf-8 -*-

import requests




url = 'http://127.0.0.1:5000/getInfo'
response = requests.get(url)
print(response.text)