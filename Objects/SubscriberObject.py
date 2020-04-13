from Objects.PersonObject import Person
from Repository import SubscribersRepository

class Subscriber(Person):
    def __init__(self, person_id):
        person = SubscribersRepository.getPerson(person_id)
        person_id = person_id
        name = person["name"]
        address = person["address"]
        super().__init__(person_id, name, address)
    
    @staticmethod
    def AddSubscriber(name, address):
            subscriberToAdd = {"name": name, "address": address}
            newSubscriberId = SubscribersRepository.addSubscriber(subscriberToAdd)
            print("Given Id: " + newSubscriberId)
            return Subscriber(newSubscriberId)
