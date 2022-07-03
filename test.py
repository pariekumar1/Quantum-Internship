import urllib.request

url = "https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdatadropper.z13.web.core.windows.net%2Ftest.txt&data=05%7C01%7C%7C5cf622addf2c493a205d08da59283675%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C637920326495749362%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=w7f8ZVficpq0PnNo5E6lcoAJz6Lf1UxVklzNHNhAUko%3D&reserved=0"

file = urllib.request.urlopen(url)

for line in file: 
    decoded_line = line.decode("utf-8").strip()
    print(decoded_line)
    