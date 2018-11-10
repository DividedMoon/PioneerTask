#静态网页的爬取

import requests
from bs4 import BeautifulSoup

url = 'https://pvp.qq.com/web201605/herodetail/199.shtml'
r = requests.get(url)
r.encoding = r.apparent_encoding
demo = r.text

soup = BeautifulSoup(demo, 'html.parser')

skillname = []
skilldesc = []
for x in soup.find_all('p', 'skill-name'):
    skillname.append(x.b.string)
for x in soup.find_all('p', 'skill-desc'):
    skilldesc.append(x.string)

for i in range(len(skillname)-1):
    print(skillname[i])
    print(skilldesc[i])
    print()
