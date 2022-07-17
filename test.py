from pickle import FALSE
import urllib.request
import matplotlib.pyplot as pp
import numpy as np
from dateutil import parser
import statistics
 
# The URL to get the Quantum Lab Data Files
 
urlFiles = "https://datadropper.z13.web.core.windows.net"
 
# read the data from the URL into file and write it to a local file labfiles.txt
 
file1 = urllib.request.urlopen(urlFiles)
 
fh1 = open('labfiles.txt', 'w+')
 
for line in file1:
    decoded_line = line.decode("utf-8").strip()
    fh1.write(decoded_line)
    fh1.write('\n')
 
fh1.close()
 
# Open the filehandle to write the DataFile and the Rules it supports
 
fh2 = open('rulessupported.txt', 'w+')
 
# Load the data to split the filenames into an array
 
filesdata = np.loadtxt(fname = 'labfiles.txt', dtype = 'str')
# print(filesdata)
 
url1 = "https://datadropper.z13.web.core.windows.net/"
 
for i in range(len(filesdata)):
 
    if (filesdata[i] == 'data.csv' or filesdata[i] == 'test.txt'):
        fh2.write('Skip ')
        fh2.write(filesdata[i])
        fh2.write(' since it does not exist!')
        fh2.write('\n')
        # print("Skip since it does not exist: ", filesdata[i])
        continue
 
    # Append the filename to the URL to get the lab data for this file
 
    url = url1 + filesdata[i]
 
    # print(url)
    fh2.write(url)
    fh2.write('\n')
 

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
    # print(data)
 
    # Split the data into X and Y arrays
 
    X=[]
    Y=[]
 
    for i in range(len(data)):
        for j in range(2):
            if j == 0:
                X.append(parser.parse(data[i][j]))
            else:
                Y.append(float(data[i][j]))
 
    # print(X)
    # print(Y)
 
    # Calculate the mean and standard deviation
 
    m = statistics.mean(Y)
    sd = statistics.stdev(Y)
 
    # print ("Mean = ", m)
    # print ("SD = ", sd)
 
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
 
    # Capture the absolute distance from "mean" and subtract 3*sd
 
    for i in range(len(Y)):
        Rule1.append(abs(Y[i] - m) - 3*sd)
 
    # print("Rule1 = ", Rule1)
 
    # Check if any point in Rule1 is postive after subtracting 3*sd
    # If its positive then its outside of Zone A
 
    result = any(Rule1)
 
    if (result):
        fh2.write('Western Electric Rule1 is satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule1 is satisfied on this chart!")
    else:
        fh2.write('Western Electric Rule1 is NOT satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule1 is NOT satisfied on this chart!")
 
    # Capture the distance from the mean and whether the point is above or below the "mean" line
 
    Rule = []
    RuleSign = []
 
    # Calculate the distance of the point from "mean"
    # Note that the point can be either above or below the "mean" line
 
    for i in range(len(Y)):
        Rule.append(Y[i] - m)
 
    # print("Rule = ", Rule)
 
    # Note whether the point is above or below the "mean" line in RuleSign
    # +1 means above the "mean" line and -1 means below the "mean" line
 
    RuleSign = np.sign(Rule)
 
    # print("RuleSign = ", RuleSign)
 
    # Let's check for Rule2
 
    Rule2Check = []
    foundTwo = False
 
    # Get the absolute distance from "mean" and subtract 2 * sd to capture if the point is in Zone A or outside relative to the "mean" line
 
    for i in range(len(Rule)):
        Rule2Check.append(abs(Rule[i]) - 2*sd)
 
    # print("Rule2Check = ", Rule2Check)
 
    # Walk through Rule2Check to see if we have two consecutive positive points on the same side of "mean"
    # The RuleSign captures which side of the "mean" line the point lies
 
    for i in range(len(Rule2Check)):
        if (i > 0 and Rule2Check[i-1] > 0 and Rule2Check[i] > 0
            and RuleSign[i-1] == RuleSign[i]):
            # print("Rule2: i = ", i)
            foundTwo = True
            break
 
    if (foundTwo):
        fh2.write('Western Electric Rule2 is satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule2 is satisfied on this chart!")
    else:
        fh2.write('Western Electric Rule2 is NOT satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule2 is NOT satisfied on this chart!")
   
    # Let's check for Rule3
 
    Rule3Check = []
    foundFive = False
 
    # Get the absolute distance from "mean" and subtract sd to capture if the point is in Zone B or outside relative to the "mean" line
 
    for i in range(len(Rule)):
        Rule3Check.append(abs(Rule[i]) - sd)
 
    # print("Rule3Check = ", Rule3Check)
 
    # Walk through Rule3Check to see if we have five consecutive positive points on the same side of "mean"
    # The RuleSign captures which side of the "mean" line the point lies
 
    for i in range(len(Rule3Check)):
        if (i > 3 and Rule3Check[i-4] > 0 and Rule3Check[i-3] > 0 and Rule3Check[i-2] > 0 and Rule3Check[i-1] > 0 and Rule3Check[i] > 0
            and RuleSign[i-4] == RuleSign[i-3] == RuleSign[i-2] == RuleSign[i-1] == RuleSign[i]):
            # print("Rule3: i = ", i)
            foundFive = True
            break
 
    if (foundFive):
        fh2.write('Western Electric Rule3 is satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule3 is satisfied on this chart!")
    else:
        fh2.write('Western Electric Rule3 is NOT satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule3 is NOT satisfied on this chart!")
 
    # Let's check for Rule4
 
    Rule4Check = []
    foundNine = False
 
    # Get the absolute distance from "mean" and to capture if the point is in Zone C or outside relative to the "mean" line
 
    for i in range(len(Rule)):
        Rule4Check.append(abs(Rule[i]))
 
    # print("Rule4Check = ", Rule4Check)
 
    # Walk through Rule4Check to see if we have nine consecutive positive points on the same side of "mean"
    # The RuleSign captures which side of the "mean" line the point lies
 
    for i in range(len(Rule4Check)):
        if (i > 7 and Rule4Check[i-8] > 0 and Rule4Check[i-7] > 0 and Rule4Check[i-6] > 0 and Rule4Check[i-5] > 0 and Rule4Check[i-4] > 0 and Rule4Check[i-3] > 0 and Rule4Check[i-2] > 0 and Rule4Check[i-1] > 0 and Rule4Check[i] > 0 and
            RuleSign[i-8] == RuleSign[i-7] == RuleSign[i-6] == RuleSign[i-5] == RuleSign[i-4] == RuleSign[i-3] == RuleSign[i-2] == RuleSign[i-1] == RuleSign[i]):
            # print("Rule4: i = ", i)
            foundNine = True
            break
 
    if (foundNine):
        fh2.write('Western Electric Rule4 is satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule4 is satisfied on this chart!")
    else:
        fh2.write('Western Electric Rule4 is NOT satisfied on this chart!')
        fh2.write('\n')
        # print("Western Electric Rule4 is NOT satisfied on this chart!")
 
fh2.close()