from pymongo import MongoClient
import os

dbconfig_file=os.pardir+'/DB.cfg'
f=open(dbconfig_file)
dbString=f.read()
_DB_SETTINGS=eval(dbString)

class DBInfo:
    host=_DB_SETTINGS['host']
    port=_DB_SETTINGS['port']
    db=_DB_SETTINGS['db']


def GetDB():
    client=MongoClient(_DB_SETTINGS['host'],int(_DB_SETTINGS['port']))
    db=client[DBInfo.db]
    return db


if __name__ == '__main__':
    db=GetDB(_DB_SETTINGS['db'])
    for i in db.branches.find({}):
        print(i)