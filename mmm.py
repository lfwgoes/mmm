# Usability Tester for Mini Mouse Macro files

import math

# Reading log lines from file
logFile = open('asdas.mmmacro','r')
logLines = logFile.readlines()
logFile.close()

# Spliting log lines into columns
logData = []
for line in logLines:
    logData.append(line.rstrip().split('|',5))

# Number of clicks	
nc = 0
for logEntry in logData:
	if logEntry[4] == " Left Click Down":
		nc = nc + 1
	
print "Number of Clicks: " + str(nc)
	
# Task time 
tt = 0
for logEntry in logData:
	tt = tt + int(logEntry[3])

print "Task time: " + str(tt) + " ms"
 
# Mean wait time between clicks			
print "Mean Wait Time Between Clicks: " + str(tt/nc) + " ms"

# Mouse distance covered
md = 0
p1 = (800,800)
for logEntry in logData:
	if logEntry[4] == " Mouse Movement":
		p2 = (int(logEntry[1]),int(logEntry[2]))
		md = md + math.hypot(p2[0] - p1[0], p2[1] - p1[1])
		p1 = p2
	
print "Mouse distance covered: " + str(int(md))

	
