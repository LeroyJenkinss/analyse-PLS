# PersonObject.py is een class wat overgeerft wordt door andere classes, nou dat betekent dus dat er nog 2 classes toegevoegd moeten
# Mag je lekker naar de class diagram kijken om welke 2 classes het gaat
# Succes, Okee doei 

from Objects.PersonObject import Person
from Repository import SubscribersRepository

class Subscriber(Person):
    def __init__(self, person_id):
        person = SubscribersRepository.getPerson(person_id)
        person_id = person["id_subscriber"]
        name = person["name"]
        address = person["address"]
        super().__init__(person_id, name, address)
    
    @staticmethod
    def AddSubscriber():
        # doe hier een call naar de SubscribersRepository.addSubsriber(name, address) wat een subscriber toevoegt en een nieuwe instance van Subscriber maakt. 
        # Kijk naar AddBook() in BookObject.py als voorbeeld
        pass
