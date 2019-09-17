# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:39:37 2018

@author: User
"""

import requests
import json
import csv

url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20181005&stockNo=2887&_=1538746599700'

res = requests.get(url_twse)
s = json.loads(res.text)

outputfile = open(r'C:\Users\User\Desktop\台灣證券市場(台新金).csv', 'w', newline='' )
outputwriter = csv.writer(outputfile)
outputwriter.writerow(s['title'])
outputwriter.writerow(s['fields'])
for data in (s['data']):
    outputwriter.writerow(data)
    
outputfile.close()

    