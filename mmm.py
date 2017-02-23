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
	
# Wait time between clicks	
wtbc = 0
wt = 0
for logEntry in logData:
	if logEntry[4] == " Left Click Down":
		wtbc = wtbc + int(logEntry[3]) + wt
		wt = 0
	else:
		wt = wt + int(logEntry[3])
	
print "Wait Time Between Clicks: " + str(wtbc) + " ms"
	
# Number of clicks	
nc = 0
for logEntry in logData:
	if logEntry[4] == " Left Click Down":
		nc = nc + 1
	
print "Number of Clicks: " + str(nc)

# Mouse distance covered
md = 0
p1 = (800,800)
for logEntry in logData:
	if logEntry[4] == " Mouse Movement":
		p2 = (int(logEntry[1]),int(logEntry[2]))
		md = md + math.hypot(p2[0] - p1[0], p2[1] - p1[1])
		p1 = p2
	
print "Mouse distance covered: " + str(int(md))

 