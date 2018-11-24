from flask import Flask, render_template
import requests
import json
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def hello_flask():
    return render_template('true-index.html')


@app.route('/id/<number>')
def index(number):
    url = "https://pvp.qq.com/web201605/herodetail/"+str(number)+".shtml"
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    demo = html.text

    soup = BeautifulSoup(demo, "html.parser")

    hero_title = soup.find('h3', 'cover-title').string
    hero_name = soup.find('h2', 'cover-name').string

    skill_name = []
    skill_desc = []
    for i in soup.find_all('p', 'skill-name'):
        skill_name.append(i.b.string)
    for i in soup.find_all('p', 'skill-desc'):
        skill_desc.append(i.string)
    skill_name.pop()
    skill_desc.pop()

    return render_template('index.html',
                           hero_name=hero_name,
                           hero_title=hero_title,
                           skill_desc=skill_desc,
                           skill_name=skill_name,
                           hero_id=number
                           )


@app.route('/item/<item_id>')
def show_item(item_id):
    url = 'https://pvp.qq.com/web201605/js/item.json'

    res = urllib.request.urlopen(url)
    item_name = []
    item_price = []
    item_total_price = []
    des1 = []
    des2 = []
    item_json = json.loads(res.read())
    for i in item_json:
        if i['item_id'] == item_id:
            item_name.append(i['item_name'])
            item_price.append(i['price'])
            item_total_price.append(i['total_price'])
            des1.append(i['des1'].replace('<p>', '').replace('<br>', ' ').replace('</p>', ''))
            if 'des2' in i:
                des2.append(i['des2'].replace('<p>', '').replace('<br>', ' ').replace('</p>', ''))
    return render_template('item.html',
                           name=item_name,
                           price=item_price,
                           total_price=item_total_price,
                           des1=des1,
                           des2=des2
                           )


@app.route('/hello')
def hello_world():
    return 'Hello,World!'


if __name__ == '__main__':
    app.run(debug=True)

