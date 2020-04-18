import hashlib 
import urllib.request
from urllib.parse import urlparse
import ssl
import os
import timeit
import pandas as pd

start = timeit.default_timer()

ssl._create_default_https_context = ssl._create_unverified_context

url='https://swd.bits-goa.ac.in/media/'
number='9120273977'

print("Fetching IDs...",end='\r')
tables = pd.read_html("https://swd.bits-goa.ac.in/search1/?name=&bitsId=2&branch=&hostel=&room=")
data=list(tables[0]['Student ID'])
data.sort(reverse=True)
os.mkdir('Images')
for item in data:
    hash=((hashlib.md5((number+item).encode()).hexdigest()))
    try:
        urllib.request.urlretrieve((url+hash+'.jpg').rstrip(), os.path.join(os.getcwd(),'Images', str(item+'.jpg')))
        print('Retreiving:',item,end='\r')
    except:
        continue
stop = timeit.default_timer()
print('Photos retreived successfull','|','Time taken:',stop-start)