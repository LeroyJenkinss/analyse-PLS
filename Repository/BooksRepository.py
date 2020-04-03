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
class book:
    def __init__(self):
        with open('../Data/AllSubscribers.json', 'r') as targetJsonSub:
            allSubscribers = targetJsonSub.read()
            self.dict_allsub = json.loads(allSubscribers)


        with open('../Data/AllLoanedBooks.json', 'r') as targetJsonLBooks:
             allLoanedBooks = targetJsonLBooks.read()
             self.dict_allLoanedBooks = json.loads(allLoanedBooks)

        with open('../Data/AllBooks.json', 'r') as bookJsonContent:
            allbooks = bookJsonContent.read()
            self.dict_books = json.loads(allbooks)

    def add2BookJson(self,dict2json):
     with open('../Data/AllBooks.json') as targetJson:
        oldJson = json.load(targetJson)

        oldJson.append(dict2json)
        with open('../Data/AllBooks.json', mode='w') as newDict2Json:
           newDict2Json.write(json.dumps(oldJson, indent=2))







sample = {
           "id_book": 3,
           "bookItems": 3,
           "title": "De drie en een half biggetjes",
           "author" : "Sir Henk",
           "genre" : "Science-Fictins"
       }

print((book().dict_books[1]))

