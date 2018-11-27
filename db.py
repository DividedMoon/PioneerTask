import pymysql


def get_hero_db(string):
    db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='pioneer')
    cursor = db.cursor()
    sql = "select * from herolist where cname='{}'".format(string)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result


def get_item_db(item):
    db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='pioneer')
    cursor = db.cursor()
    sql = "select * from itemlist where item_name='{}'".format(item)
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result
