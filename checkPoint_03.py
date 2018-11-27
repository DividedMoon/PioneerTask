from flask import Flask
from flask import request, render_template
import requests
from  db import get_item_db, get_hero_db
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/item', methods=('GET', 'POST'))
def test():
    user = None
    if request.method == 'POST':
        user = request.values.get("item_name")
    result = get_item_db(user)

    item_name = result[0][2]
    item_price = result[0][4]
    item_total_price = result[0][5]
    des1 = result[0][6].replace('<p>', '').replace('<br>', ' ').replace('</p>', '')
    des2 = "这个装备只有那一个效果啦"
    if 'des2' in result[0]:
        des2 = result[0][7].replace('<p>', '').replace('<br>', ' ').replace('</p>', '')
    return render_template('item.html', name=user,
                           item_name=item_name,
                           item_price=item_price,
                           item_total_price=item_total_price,
                           des1=des1,
                           des2=des2)


@app.route('/hero', methods=('GET', 'POST'))
def hero():
    hero_name = None
    if request.method == 'POST':
        hero_name = request.values.get("hero_name")

    result = get_hero_db(hero_name)
    hero_number = str(result[0][1])
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
    return render_template('hero.html',
                           hero_id=hero_number,
                           hero_name=hero_name,
                           hero_title=result[0][3],
                           skill_name=skill_name,
                           skill_desc=skill_desc)


if __name__ == '__main__':
    app.run(debug=True)
