#!/usr/bin/env python3

# This is a  simple python programe to download the picture in a specific web page
#
import re
import urllib

req = urllib.urlopen('http://www.imooc.com/course/program')
buf = req.read()
listurl = re.findall(r'http:.+\.jpg', buf)
i = 1
for url in listurl:
    print("Downloading pic %d ...") %i
    f = open(str(i)+'.jpg', 'w')
    req = urllib.urlopen(url)
    buf = req.read()
    f.write(buf)
    i=i+1

