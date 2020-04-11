# LoanedBooksRepository.py moet een vergelijkbare setup hebben als BooksRepository.py Alleen dan, you guessed it, voor Data/AllLoanedBooks.json
# Zie BooksRepository.py voor verdere toelichting
import json
from shutil import copyfile
import datetime as dt
from pathlib import Path

def readJson():
    with open('../Data/AllLoanedBooks.json', 'r') as bookJsonContent:
        allbooks = bookJsonContent.read()
        dict_books = json.loads(allbooks)
    
    return dict_books

def getNewHighestId():
    jsonAsDict = readJson()
    listAllIds = jsonAsDict.keys()
    return str(int(max(listAllIds)) + 1)

def addBookToJsonAndReturnId(loanedBookToAdd):    
    newId = getNewHighestId()
    with open('../Data/AllLoanedBooks.json') as targetJson:
        oldJson = json.load(targetJson)
        oldJson[newId] = loanedBookToAdd
    with open('../Data/AllLoanedBooks.json', mode='w') as newDict2Json:
        newDict2Json.write(json.dumps(oldJson, indent=2))

    return newId

def getLoanedBookId(id):
    jsonDict = readJson()
    if isinstance(id, int):
         id = str(id)

    return jsonDict[id]

def returnBook(loanedBookToReturn):
    loanId = getLoanedBookId(loanedBookToReturn.id_book)  
    with open('../Data/AllLoanedBooks.json') as targetJson:
        oldJson = json.load(targetJson)
        oldJson[loanId] = loanedBookToReturn
    with open('../Data/AllLoanedBooks.json', mode='w') as newDict2Json:
        newDict2Json.write(json.dumps(oldJson, indent=2))

    return loanId

def createBackup():
    backUpPath = "../Data/Backup/{}/AllLoanedBooks.json".format(dt.date.today())
    if not Path(backUpPath).exists():
        Path().mkdir(parents=True, exist_ok=True)
        copyfile('../Data/AllLoanedBooks.json', backUpPath)

def recoverBackup(date):
    backUpPath ='../Data/Backup/{}/AllLoanedBooks.json'.format(date)
    copyfile(backUpPath, '../Data/AllLoanedBooks.json')
