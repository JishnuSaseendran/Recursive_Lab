'''
Problem 13: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.

'''
import sys
import tablib
def parse_csv(filename,d,c):
   return [x[:-1].split(d) for x in open(filename,'r').readlines() if x[0]!=c]
filename=sys.argv[1]
delim=raw_input("Enter the delimiter:")
comment=raw_input("Enter the comment indicator:")
parse_csv(filename,delim,comment)
data = tablib.Dataset()
for i in parse_csv(filename,delim,comment):
   data.append(i)
with open('test.xls', 'wb') as f:
   f.write(data.xls)






