import json
from shutil import copyfile
import datetime as dt
from pathlib import Path

def readJson():
    with open('Data/AllBooks.json', 'r') as bookJsonContent:
        allbooks = bookJsonContent.read()
        dict_books = json.loads(allbooks)
    
    return dict_books

def getNewHighestId():
    jsonAsDict = readJson()
    listAllIds = [int(id) for id in jsonAsDict.keys()]
    return str(max(listAllIds) + 1)

def getBook(id):
    jsonDict = readJson()
    if isinstance(id, int):
         id = str(id)

    return jsonDict[id]
       
def addBookToJsonAndReturnId(bookToAdd):    
    newId = getNewHighestId()
    with open('Data/AllBooks.json') as targetJson:
        oldJson = json.load(targetJson)
        oldJson[newId] = bookToAdd
    with open('Data/AllBooks.json', mode='w') as newDict2Json:
        newDict2Json.write(json.dumps(oldJson, indent=2))

    return newId

def createBackup():
    backUpPath ='Data/Backup/{}'.format(dt.date.today())
    Path(backUpPath).mkdir(parents=True, exist_ok=True)
    copyfile('Data/AllBooks.json', backUpPath + "/AllBooks.json")

def recoverBackup(date):
    backUpPath ='Data/Backup/{}/AllBooks.json'.format(date)
    copyfile(backUpPath, 'Data/AllBooks.json')

def removebook(book_id):
    if isinstance(book_id, int):
         book_id = str(book_id)
         
    jsonDict = readJson()
    del jsonDict[book_id]
    with open('Data/AllBooks.json', mode='w')as f:
        f.write(json.dumps(jsonDict, indent=2))