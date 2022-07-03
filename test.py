import urllib.request

url = "https://datadropper.z13.web.core.windows.net/data.csv"

file = urllib.request.urlopen(url)

for line in file:

    decoded_line = line.decode("utf-8").strip()

    print(decoded_line)
    
    print("end of data list")
      
    