'''
Problem 3: Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.
'''

import os
def filedet(dir):
	file=os.listdir(dir)
	for item in file:
		stime = os.stat(os.path.abspath(os.path.join(dir,item))).st_ctime
		mtime = os.stat(os.path.abspath(os.path.join(dir,item))).st_mtime
##	print stime
##	print mtime	
		print item,'  Length = ',len(item),'  Start Time = ',stime,'  Modification Time = ',mtime    
filedet('/home/jishnu/tasks/task 21/2. Working With Data')
