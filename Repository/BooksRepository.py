# Booksrepository moet informatie ophalen van de json bestandje, en moet ook informatie weg kunnen schrijven naar de bijbehorende json bestandje.
# In dit geval is het Data/AllBooks.Json begin eerst met een GetAll methode waarbij een dictionary van Subscribers terug komt. 
# Ik zou dit in een dictionary plaatsen met de subscriberId als key, met een innerdictionary waarbij de keys de atributen zijn van
# het Json bestandje samen met de values.
# 
# Voorbeeld hoe de dictionary uit moet zien:
# allSubscribers = 
# {
#   1 : {
#           "bookItems": 3,
#           "title": "De drie biggetjes",
#           etc.
#       }
# }
# 
# De methodes worden aangeroepen in de Objects (classes) waarbij de repository hoort. (Voorbeeld van een call vanuit een class: BooksRepository.GetAll())
# Als jullie enthousiast zijn over deze shizzle en al snel klaar zijn kunnen jullie ook een tweede methode maken genaamd
# GetSubscriber(subscriberId) Die dan de get GetAll() methode aan roept en vervolgens op basis van subscriberId de bijbehorende innerdictionary teruggeeft
#
# Python heeft een paar goede tools hiervoor in de module JSON, zit waarschijnlijk ook een functie die json bestandjes gelijk inlaad. 
# Not sure tho, mogen jullie zelf uitvogelen, ma dudes
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
    listAllIds = jsonAsDict.keys()
    return str(int(max(listAllIds)) + 1)

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
    backUpPath ='Data/Backup/{}/AllBooks.json'.format(dt.date.today())
    if not Path(backUpPath).exists():
        Path(backUpPath).mkdir(parents=True, exist_ok=True)
        copyfile('Data/AllBooks.json', backUpPath)

def recoverBackup(date):
    backUpPath ='Data/Backup/{}/AllBooks.json'.format(date)
    copyfile(backUpPath, 'Data/AllBooks.json')

def removebook(book_id):

    jsonDict = readJson()
    del jsonDict[book_id]
    with open('Data/AllBooks.json', mode='w')as f:
        f.write(json.dumps(jsonDict, indent=2))


