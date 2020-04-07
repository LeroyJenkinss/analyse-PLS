# SubscribersRepository.py moet een vergelijkbare setup hebben als BooksRepository.py Alleen dan, you guessed it, voor Data/AllSubscribers.json
# Zie BooksRepository.py voor verdere toelichting

import json

def readJson():
    with open('../Data/AllSubscribers.json', 'r') as targetJsonSub:
        allSubscribers = targetJsonSub.read()
        dict_allsub = json.loads(allSubscribers)

    return dict_allsub

def getPerson(id):
     jsonAsDict = readJson()
     if isinstance(id, int):
         id = str(id)
     return jsonAsDict[id]

def getNewHighestId():
    jsonAsDict = readJson()
    listAllIds = jsonAsDict.keys()
    return str(int(max(listAllIds)) + 1)

def addSubscriber(subscriberToAdd):
    newId = getNewHighestId()
    with open('../Data/AllSubscribers.json') as targetJson:
        oldJson = json.load(targetJson)
        oldJson[newId] = subscriberToAdd
    with open('../Data/AllSubscribers.json', mode='w') as newDict2Json:
        newDict2Json.write(json.dumps(oldJson, indent=2))

    return newId


