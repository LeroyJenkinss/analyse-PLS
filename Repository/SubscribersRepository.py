# SubscribersRepository.py moet een vergelijkbare setup hebben als BooksRepository.py Alleen dan, you guessed it, voor Data/AllSubscribers.json
# Zie BooksRepository.py voor verdere toelichting

import json
from shutil import copyfile
import datetime as dt
from pathlib import Path

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

def addSubsriber(name, address):
    pass
    # Voeg nieuwe subscriber toe door de hoogste id op te halen getNewHighestId()
    # voeg toe aan json bestandje met naam en adress als parameter

def createBackup():
    backUpPath ='../Data/Backup/{}/AllSubscribers.json'.format(dt.date.today())
    if not Path(backUpPath).exists():
        Path(backUpPath).mkdir(parents=True, exist_ok=True)
        copyfile('../Data/AllSubscribers.json', backUpPath)

def recoverBackup(date):
    backUpPath ='../Data/Backup/{}/AllSubscribers.json'.format(date)
    copyfile(backUpPath, '../Data/AllSubscribers.json')
