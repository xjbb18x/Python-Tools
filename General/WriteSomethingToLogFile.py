#Write something to a logfile

import os

logfilename = r"C:\temp\logtest.txt"

if os.path.exists(logfilename):
	os.remove(logfilename)
logfile = open(logfilename, 'w')
		
something = "Hello World"
logfile.write(something)

##or record the date and time:
#import time
#now = time.now(time.strftime("%Y%m%d %X"))
#logfile.write(now)

logfile.flush()
logfile.close()
