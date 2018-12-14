import urllib.request as req

data = req.urlopen('https://collinmurch.com').read()

split = data.decode('utf-8').split('href="')

urls = []

for item in split:
    if item.startswith('https:'):
       urls.append(item.split("\"")[0])

print(urls)
