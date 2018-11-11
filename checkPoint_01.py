import requests
from bs4 import BeautifulSoup

number = input("Please input number to check the skill : ")
url = 'https://pvp.qq.com/web201605/herodetail/'+number+'.shtml'
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
heroTitle = soup.find('h3', 'cover-title')
heroName = soup.find('h2', 'cover-name')

print(heroTitle.string+' : '+heroName.string)
for i in range(len(skillname)-1):
    print(skillname[i])
    print(skilldesc[i])
    print()
