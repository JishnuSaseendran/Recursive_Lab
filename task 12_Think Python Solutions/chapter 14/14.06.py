import urllib

zipcode = '02492'

url = 'http://uszip.com/zip/' + zipcode
conn = urllib.urlopen(url)

for line in conn.fp:
    line = line.strip()
    if 'Population' in line:
        print "\n Population is" 
        print line
    if 'Longitude' in line: 
        print "\ Longitude is" 
        print line
    if 'Latitude' in line: 
        print "\n Latitude is" 
        print line

conn.close()
