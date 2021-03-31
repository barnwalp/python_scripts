import requests


url = "https://unsplash.com/napi/search/photos?query=motivational%20quotes&per_page=50&page=5&xp="
r = requests.get(url)
data = r.json()

for item in data['results']:
    name = item['id']
    urls = item['urls']['regular']
    with open(name+".jpg", "wb") as f:
        f.write(requests.get(urls).content)
