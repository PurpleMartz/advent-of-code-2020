# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 06:56:29 2021

@author: Marty
"""

import requests
from os import makedirs

for i in range(1, 26):
    cookies = eval(open('Secret/adventCookie.txt', 'r').read())
    url = 'https://adventofcode.com/2020/day/' + str(i) + '/input'
    response = requests.get(url, cookies=cookies)
    response.raise_for_status() # ensure we notice bad responses
    num = "%02d" % (i,)
    makedirs(num)
    file = open(num + '/Problem ' +  num + ' Data.txt', 'w')
    file.write(response.text)
    file.close()