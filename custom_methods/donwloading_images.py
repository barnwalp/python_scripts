import requests

"""
url = "https://unsplash.com/napi/search/photos?query=motivational%20quotes&per_page=50&page=5&xp="
r = requests.get(url)
data = r.json()

for item in data['results']:
    name = item['id']
    urls = item['urls']['regular']
    with open(name+".jpg", "wb") as f:
        f.write(requests.get(urls).content)
"""

url = "https://directory.ntschools.net/api/System/GetAllSchools"
r = requests.get(url)
data = r.json()
# print(data)

for item in data:
    school_name = item['schoolName']
    school_type = item['schoolType']
    area = item['electorate']
    region = item['decsRegion']
    government_school = item['isGovernment']
    code = item['itSchoolCode']
    pre_school = item['isPreSchool']
    # newline character can't beol']
    nl = '\n'
    print(f'{school_name}{nl}')
