from flask import Flask, render_template
import requests
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
                           skill_name=skill_name
                           )


@app.route('/hello')
def hello_world():
    return 'Hello,World!'


if __name__ == '__main__':
    app.run(debug=True)

