import pymysql
from config import config

def query(sql):
    db = pymysql.connect(host='localhost', user='root', password=config['MYSQL_PASSWORD'], database=config['DATABASE_NAME'], charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()

        #print('query success')

        # print('query success')
    except:
        # print('query loss')
        result = None
        db.rollback()
    cur.close()
    db.close()
    return result