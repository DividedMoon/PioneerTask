from flask import Flask
from flask import request, render_template
import json
import urllib.request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('true-index.html')


user = 'inspector'
item_total_price = "And I've been trying to fix it up."
item_price = 'That means there is something wrong.'
item_name = "If you can see this sentence."
des1 = 'But I always failed.'
des2 = 'So here it is.:)'


@app.route('/item', methods=('GET', 'POST'))
def test():
    global user, item_total_price, item_price, item_name, des1, des2
    if request.method == 'POST':
        user = request.values.get("item_name")

    url = 'https://pvp.qq.com/web201605/js/item.json'
    res = urllib.request.urlopen(url)
    item_json = json.loads(res.read())
    check_name = user
    for i in item_json:
        if i['item_name'] == check_name:
            item_name = i['item_name']
            item_price = i['price']
            item_total_price = i['total_price']
            des1 = i['des1'].replace('<p>', '').replace('<br>', ' ').replace('</p>', '')
            if 'des2' in i:
                des2 = i['des2'].replace('<p>', '').replace('<br>', ' ').replace('</p>', '')
    return render_template('test.html', name=user,
                           item_name=item_name,
                           item_price=item_price,
                           item_total_price=item_total_price,
                           des1=des1,
                           des2=des2)


hero_title = 'None'
hero_name = 'None'
hero_ename = 'None'


@app.route('/hero', methods=('GET', 'POST'))
def hero():
    global hero_title, hero_name, hero_ename
    if request.method == 'POST':
        hero_name = request.values.get("hero_name")

    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    res = urllib.request.urlopen(url)
    hero_json = json.loads(res.read())
    for i in hero_json:
        if i['cname'] == hero_name:
            hero_title = i['title']
            hero_ename = i['ename']
    hero_number = str(hero_ename)
    anurl = 'https://pvp.qq.com/web201605/herodetail/' + hero_number + '.shtml'
    r = requests.get(anurl)
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    skill_name = []
    skill_desc = []
    for x in soup.find_all('p', 'skill-name'):
        skill_name.append(x.b.string)
    for x in soup.find_all('p', 'skill-desc'):
        skill_desc.append(x.string)
    return render_template('index.html',
                           hero_id=hero_number,
                           hero_name=hero_name,
                           hero_title=hero_title,
                           skill_name=skill_name,
                           skill_desc=skill_desc)


if __name__ == '__main__':
    app.run(debug=True)
