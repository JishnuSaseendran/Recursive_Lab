


import urllib, re

data = re.search('"([0-9.]*)"', urllib.urlopen("http://httpbin.org/get").read()).group(1)
print data


