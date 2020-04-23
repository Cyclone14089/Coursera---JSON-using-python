import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
content = urllib.request.urlopen(url).read()
print("Retrieved",len(content),"characters")

info = json.loads(content)
count = 0
s = 0

for item in info["comments"] :
    s = s + item['count']
    count = count + 1

print("Count:",count)
print("Sum:",s)