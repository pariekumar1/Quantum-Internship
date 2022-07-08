import urllib.request
import matplotlib.pyplot as pp
import numpy as np
 

# The URL to get the Quantum Lab Data
url = "https://datadropper.z13.web.core.windows.net/data.csv"
 
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
            X.append(data[i][j])
        else:
            Y.append(data[i][j])
 
print(X)
print(Y)
 
# Graph the data
 
pp.plot(X, Y, label = 'Date/Value Plot')
pp.xlabel('Date')
pp.ylabel('Value')
pp.title('Lab Data')
pp.legend()
pp.show()