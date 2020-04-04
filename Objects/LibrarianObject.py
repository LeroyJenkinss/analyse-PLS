# PersonObject.py is een class wat overgeerft wordt door andere classes, nou dat betekent dus dat er nog 2 classes toegevoegd moeten
# Mag je lekker naar de class diagram kijken om welke 2 classes het gaat
# Succes, Okee doei 

from Objects.PersonObject import Person
from Repository import SubscribersRepository

class Librarian(Person):
    def __init__(self):
        person_id = int(SubscribersRepository.getHighestId()) + 1
        name = "Librarian"
        address = "Library"
        super().__init__(person_id, name, address)


