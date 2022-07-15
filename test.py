from pickle import FALSE
import urllib.request
import matplotlib.pyplot as pp
import numpy as np
from datetime import datetime
#from dateutil import parser
import statistics
 
# The URL to get the Quantum Lab Data
 
url = "https://datadropper.z13.web.core.windows.net/flow.csv"
 
# read the data from the URL into file and write it to a local file labdata.txt
 
file = urllib.request.urlopen(url)
 
fh = open('labdata.txt', 'w+')
 
for line in file:
    decoded_line = line.decode("utf-8").strip()
    fh.write(decoded_line)
    fh.write('\n')
 
fh.close()
 
# Load the data to split and graph
 
data = np.loadtxt(fname = 'labdata.txt', dtype = 'str', delimiter = ',')
print(data)
 
# Split the data into X and Y arrays
 
X=[]
Y=[]
 
for i in range(len(data)):
    for j in range(2):
        if j == 0:
            X.append(datetime.strptime(data[i][j], '%d/%m/%Y %H:%M:%S'))
            #X.append(parser.parse(data[i][j]))
        else:
            Y.append(float(data[i][j]))
 
print(X)
print(Y)
 
# Calculate the mean and standard deviation
 
m = statistics.mean(Y)
sd = statistics.stdev(Y)
 
print (m)
print (sd)
 
# Graph the data
 
pp.plot(X, Y, label = 'Date/Value Plot')
 
pp.axhline(m, color = 'k', linestyle = 'dashed')
pp.axhline(m + sd, color = 'y', linestyle = 'dashed')
pp.axhline(m + 2*sd, color = 'y', linestyle = 'dashed')
pp.axhline(m + 3*sd, color = 'y', linestyle = 'dashed')
pp.axhline(m - sd, color = 'y', linestyle = 'dashed')
pp.axhline(m - 2*sd, color = 'y', linestyle = 'dashed')
pp.axhline(m - 3*sd, color = 'y', linestyle = 'dashed')
 
pp.xlabel('Date')
pp.ylabel('Value')
pp.title('Lab Data')
pp.legend()
pp.show()
 
# Let's check for Rule1
 
Rule1 = []
 
for i in range(len(Y)):
    Rule1.append(abs(Y[i] - m) - 3*sd)
 
 
result = any(Rule1)
 
if (result):
    print("Western Electric Rule1 is satisfied on this chart!")
else:
    print("Western Electric Rule1 is NOT satisfied on this chart!")
 

# Let's check for Rule2
 
Rule2 = []
foundTwo = False
 
for i in range(len(Y)):
    Rule2.append(abs(Y[i] - m) - 2*sd)
 
for i in range(len(Rule2)):
    if (i > 0 and Rule2[i-1] > 0 and Rule2[i] > 0):
        foundTwo = True
        break
 
if (foundTwo):
    print("Western Electric Rule2 is satisfied on this chart!")
else:
    print("Western Electric Rule2 is NOT satisfied on this chart!")
 
# Let's check for Rule3
 
Rule3 = []
foundFive = False
 
for i in range(len(Y)):
    Rule3.append(abs(Y[i] - m) - sd)
 
for i in range(len(Rule3)):
    if (i > 4 and Rule3[i-4] > 0 and Rule3[i-3] > 0 and Rule3[i-2] > 0 and Rule3[i-1] > 0 and Rule3[i] > 0):
        foundFive = True
        break
 
if (foundFive):
    print("Western Electric Rule3 is satisfied on this chart!")
else:
    print("Western Electric Rule3 is NOT satisfied on this chart!")
 
# Let's check for Rule4
 
Rule4 = []
foundNine = False
 
for i in range(len(Y)):
    Rule4.append(abs(Y[i] - m))
 
for i in range(len(Rule4)):
    if (i > 4 and Rule4[i-8] > 0 and Rule4[i-7] > 0 and Rule4[i-6] > 0 and Rule4[i-5] > 0 and Rule4[i-4] > 0 and Rule4[i-3] > 0 and Rule4[i-2] > 0 and Rule4[i-1] > 0 and Rule4[i] > 0):
        foundNine = True
        break
 
if (foundNine):
    print("Western Electric Rule4 is satisfied on this chart!")
else:
    print("Western Electric Rule4 is NOT satisfied on this chart!")
 
 
 
