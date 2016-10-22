'''
Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

$ python wget.py http://docs.python.org/tutorial/interpreter.html
saving http://docs.python.org/tutorial/interpreter.html as interpreter.html.

$ python wget.py http://docs.python.org/tutorial/
saving http://docs.python.org/tutorial/ as index.html.
'''
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

