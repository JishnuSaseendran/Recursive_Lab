'''import urllib, json

data = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
print data["ip"]
Problem 10: Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and read the IP address from there. The program should print only the IP address and nothing else.
'''

import urllib
import json

print "we will try to open this url, in order to get IP Address"
url = "http://ip.jsontest.com/"

data = json.loads(urllib.urlopen(url).read())
print data["ip"]
