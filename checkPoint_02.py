import urllib.request
import json


url = 'https://pvp.qq.com/web201605/js/item.json'

res = urllib.request.urlopen(url)

item_json = json.loads(res.read())
check_name = input("Input the item you want to check up : ")

for i in item_json:
    if i['item_name'] == check_name:
        print("{}\n售价：{}\n总价：{}".format(i['item_name'], i['price'], i['total_price']))
        print(i['des1'].replace('<p>', '').replace('<br>', ' ').replace('</p>', ''))
        if 'des2' in i:
            print(i['des2'].replace('<p>', '').replace('<br>', ' ').replace('</p>', ''))
        print()
