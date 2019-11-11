import urllib.request
import json
import requests
temp = 78
url = 'http://ec2-54-80-48-194.compute-1.amazonaws.com:5000/governor/api/v1.0/current-setpoint/'
data = json.dumps({'setPoint':str(temp)})
response = requests.put(url, data=data)
