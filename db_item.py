import pymysql
import json
import urllib.request

url = 'https://pvp.qq.com/web201605/js/item.json'
res = urllib.request.urlopen(url)
hero_json = json.loads(res.read())

db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='pioneer')
cursor = db.cursor()
table = 'itemlist'
for i in hero_json:
    keys = ', '.join(i.keys())
    values = ', '.join(['%s'] * len(i))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    if cursor.execute(sql, tuple(i.values())):
        print('Successful')
        db.commit()

db.close()
