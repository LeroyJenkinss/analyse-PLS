# SubscribersRepository.py moet een vergelijkbare setup hebben als BooksRepository.py Alleen dan, you guessed it, voor Data/AllSubscribers.json
# Zie BooksRepository.py voor verdere toelichting

import json

def openJson():
    with open('../Data/AllSubscribers.json', 'r') as targetJsonSub:
        allSubscribers = targetJsonSub.read()
        dict_allsub = json.loads(allSubscribers)

    return dict_allsub

def getPerson(id):
     jsonAsDict = openJson()
     if isinstance(id, int):
         id = str(id)
     return jsonAsDict[id]

def getHighestId():
    jsonAsDict = openJson()
    listAllIds = jsonAsDict.keys()
    return max(listAllIds)

def addSubsriber(name, address):
    pass
    # Voeg nieuwe subscriber toe door de hoogste id op te halen (getHighestId() + 1)
    # voeg toe aan json bestandje met naam en adress als parameter
