#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

URL = 'http://www.modcloth.com/shop/dresses'

req = requests.get(URL)
if req.status_code != 200:
    raise Exception('didnt get a 200 status code')

soup = BeautifulSoup(req.text, 'html.parser')

names = [a.text for a in soup.select('.product-info a')]
names = [n.lower().replace(u'’', "'") for n in names]

for name in names:
    words = name.split()
    words = filter(lambda w: 'dress' not in w, words)
    while len(words) > 2 and words[-2] == 'in':
        words = words[:-2]

    print ' '.join(words)
