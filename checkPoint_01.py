# 静态网页的爬取

import requests
from bs4 import BeautifulSoup

number = input("Please input number to check the skill : ")
heroList = {number: number, "廉颇": "105", "小乔": "106", "赵云": "107",
            "墨子": "108", "妲己": "109", "嬴政": "110",
            "孙尚香": "111", "鲁班七号": "112", "庄周": "113",
            "刘禅": "114", "高渐离": "115", "阿轲": "116",
            "钟无艳": "117", "孙膑": "118", "扁鹊": "119",
            "白起": "120", "芈月": "121", "吕布": "123",
            "周瑜": "124", "夏侯惇": "126", "甄姬": "127",
            "曹操": "128", "典韦": "129", "宫本武藏": "130",
            "李白": "131", "马可波罗": "132", "狄仁杰": "133",
            "达摩": "134", "项羽": "135", "武则天": "136",
            "老夫子": "139", "关羽": "140", "貂蝉": "141",
            "安琪拉": "142", "程咬金": "144", "露娜": "146",
            "姜子牙": "148", "刘邦": "149", "韩信": "150",
            "王昭君": "152", "兰陵王": "153", "花木兰": "154",
            "张良": "156", "不知火舞": "157", "娜可露露": "162",
            "橘右京": "163", "亚瑟": "166", "孙悟空": "167",
            "牛魔": "168", "后羿": "169", "刘备": "170",
            }
url = 'https://pvp.qq.com/web201605/herodetail/'+heroList[number]+'.shtml'
r = requests.get(url)
r.encoding = r.apparent_encoding
demo = r.text
# 获取静态网页的信息

soup = BeautifulSoup(demo, 'html.parser')
# 解析信息

skillName = []
skillDesc = []
for x in soup.find_all('p', 'skill-name'):
    skillName.append(x.b.string)
# 获取英雄的技能名称

for x in soup.find_all('p', 'skill-desc'):
    skillDesc.append(x.string)
# 获取英雄的技能说明

heroTitle = soup.find('h3', 'cover-title')
heroName = soup.find('h2', 'cover-name')
# 获取英雄的头衔和姓名

print(heroTitle.string+' : '+heroName.string)
for i in range(len(skillName)-1):
    print(skillName[i])
    print(skillDesc[i])
    print()

print("人物故事 ：")
for i in soup.find('div', 'pop-bd').p.stripped_strings:
    print(i)
