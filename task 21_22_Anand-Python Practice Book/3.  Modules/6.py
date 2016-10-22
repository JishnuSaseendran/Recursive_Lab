'''
Problem 6: Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.

$ python antihtml.py index.html
...
The Python interpreter is usually installed as /usr/local/bin/python on
those machines where it is available; putting /usr/local/bin in your
...
'''

import re
import os
import urllib
import sys
url=sys.argv[1]
if url[-1]=='/':
   basename='index.html'
else:
   basename=url.split('/')[-1]
print 'Saving  ',url,'  as ',basename
urllib.urlretrieve(url,os.getcwd()+'/'+basename)
f=open(basename,'r')
strings = re.findall(r'>[^<]+<', f.read())
for i in strings:
   print i[1:-1]


