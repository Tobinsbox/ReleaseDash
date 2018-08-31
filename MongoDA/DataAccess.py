from pymongo import MongoClient
import os

dbconfig_file=os.pardir+'\DB.cfg'
f=open(dbconfig_file)
dbString=f.read()
_DB_SETTINGS=eval(dbString)
print(_DB_SETTINGS)

def GetDB(dbName):
    client=MongoClient(_DB_SETTINGS['host'],int(_DB_SETTINGS['port']))
    db=client[dbName]
    return db


if __name__ == '__main__':
    db=GetDB('absuiterelease')
    db.eval(os.pardir+'\mongoDataPrepare\insertCycle.js')