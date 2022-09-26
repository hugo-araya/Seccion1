import requests
res = requests.get('https://www.nasa.gov')
print(res.text)