from flask import Flask
from flask import request, render_template
import json
import urllib.request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


user = 'inspector'
item_total_price = "And I've been trying to fix it up."
item_price = 'That means there is something wrong.'
item_name = "If you can see this sentence."
des1 = 'But I always failed.'
des2 = 'So here it is.:)'


@app.route('/username', methods=('GET', 'POST'))
def test():
    global user, item_total_price, item_price, item_name, des1, des2
    if request.method == 'POST':
        user = request.values.get("username")

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


if __name__ == '__main__':
    app.run(debug=True)
