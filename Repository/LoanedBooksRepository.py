# LoanedBooksRepository.py moet een vergelijkbare setup hebben als BooksRepository.py Alleen dan, you guessed it, voor Data/AllLoanedBooks.json
# Zie BooksRepository.py voor verdere toelichting
import json
from shutil import copyfile
import datetime as dt
from pathlib import Path

def readJson():
    with open('Data/AllLoanedBooks.json', 'r') as bookJsonContent:
        allbooks = bookJsonContent.read()
        dict_books = json.loads(allbooks)
    
    return dict_books

def getNewHighestId():
    jsonAsDict = readJson()
    listAllIds = [int(id) for id in jsonAsDict.keys()]
    return str(max(listAllIds) + 1)

def addBookToJsonAndReturnId(loanedBookToAdd):    
    newId = getNewHighestId()
    with open('Data/AllLoanedBooks.json') as targetJson:
        oldJson = json.load(targetJson)
        oldJson[newId] = loanedBookToAdd
    with open('Data/AllLoanedBooks.json', mode='w') as newDict2Json:
        newDict2Json.write(json.dumps(oldJson, indent=2))

    return newId

def getLoanedBook(id):
    jsonDict = readJson()
    if isinstance(id, int):
         id = str(id)

    return jsonDict[id]

def returnBook(loanedBookToReturnId, loanedBookToReturn):
    if isinstance(loanedBookToReturnId, int):
        loanedBookToReturnId = str(loanedBookToReturnId)

    with open('Data/AllLoanedBooks.json') as targetJson:
        oldJson = json.load(targetJson)
        del oldJson[loanedBookToReturnId]
        oldJson[loanedBookToReturnId] = loanedBookToReturn
    with open('Data/AllLoanedBooks.json', mode='w') as newDict2Json:
        newDict2Json.write(json.dumps(oldJson, indent=2))

    return True

def createBackup():
    backUpPath = "Data/Backup/{}".format(dt.date.today())
    Path(backUpPath).mkdir(parents=True, exist_ok=True)
    copyfile('Data/AllLoanedBooks.json', backUpPath + "/AllLoanedBooks.json")

def recoverBackup(date):
    backUpPath ='Data/Backup/{}/AllLoanedBooks.json'.format(date)
    copyfile(backUpPath, 'Data/AllLoanedBooks.json')