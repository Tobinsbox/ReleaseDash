from pymongo import MongoClient
from DB import DB_SETTING
import os


_DB_SETTINGS=DB_SETTING

class DBInfo:
    host=_DB_SETTINGS['host']
    port=_DB_SETTINGS['port']
    db=_DB_SETTINGS['db']


def GetDB():
    client=MongoClient(_DB_SETTINGS['host'],int(_DB_SETTINGS['port']))
    db=client[DBInfo.db]
    return db


if __name__ == '__main__':
    db=GetDB()
    for i in db.MachineScript.find({}):
        print(i)