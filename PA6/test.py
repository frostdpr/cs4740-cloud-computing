import re
import urllib.request, urllib.error, urllib.parse

url = 'https://ksc3ft-pa6.s3.amazonaws.com/index.html'
response = urllib.request.urlopen(url)
webContent = response.read().decode()

regex = r'<body><p> CURRENTLY:(.+?)<br>'

pattern = re.compile(regex)

print(webContent)
print(re.findall(pattern, webContent))

