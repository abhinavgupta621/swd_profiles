#Author: Abhinav Gupta(2017A4PS0907G) & Vinayak Aggarwal(2017A7PS0008G) 
#Working as on 18/04/2020 on https://swd.bits-goa.ac.in/

import hashlib 
import urllib.request
from urllib.parse import urlparse
import requests 
import json
import os, ssl
import csv
import pandas as pd 
import timeit

start = timeit.default_timer()

ssl._create_default_https_context = ssl._create_unverified_context

url='https://swd.bits-goa.ac.in/media/'

tables = pd.read_html("https://swd.bits-goa.ac.in/search1/?name=&bitsId=2&branch=&hostel=&room=")
output=list(tables[0]['Student ID'])
output.sort(reverse=True)
if not os.path.isdir('Images'):
	os.mkdir('Images')
for item in output:
	if not os.path.isdir('Images/'+item[:4]):
	  os.mkdir('Images/'+item[:4])

	tempname = ('9120273977'+item).encode('utf-8')
	try:
		urllib.request.urlretrieve(url+str(hashlib.md5(tempname).hexdigest())+'.jpg'), os.path.join(os.getcwd(),'Images/'+str(item[:4])+'/', str(item+'.jpg'))
		print('Retreiving:',item,end='\r')
	except:
		print('.')
		continue
stop = timeit.default_timer()
print('/r')
print('Time taken:',stop-start)

