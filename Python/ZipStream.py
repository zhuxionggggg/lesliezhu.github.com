#!/usr/bin/env python

from urllib2 import build_opener,install_opener,HTTPBasicAuthHandler,Request,urlopen
from urlparse import urlparse
from base64 import encodestring
import zlib


#url="https://www.freddiemac.com/sec_products_data/data/fq130606.zip"
#LOGIN="cacti_wzhao"
#PASSWD="play2winfh"

def get_handler(url):
    hdlr = HTTPBasicAuthHandler()
    hdlr.add_password("Archives",urlparse(url)[1], LOGIN,PASSWD)
    
    opener = build_opener(hdlr)
    install_opener(opener)

    req = Request(url)
    b64str = encodestring('%s:%s' % (LOGIN,PASSWD))[:-1]
    req.add_header('Authorization','Basic %s' % b64str)
    return req

f = urlopen(req)

data = f.read()
out = open("fq130606.zip","wb")
while True:
    data = f.read(1024*3)
    if len(data) == 0:
        break
    else:
        out.write(data)
        print data
