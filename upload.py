import requests

a = requests.get("http://192.168.101.4:1379/")
b = a.text
c = b.replace("<br />","\n")
print(c)
