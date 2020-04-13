from Objects.PersonObject import Person
from Repository import SubscribersRepository

class Librarian(Person):
    def __init__(self, enteredPassword):
        assert "password" == enteredPassword, "Password incorrect! (hint: password == 'password' )"
        person_id = 0
        name = "Librarian"
        address = "Library"
        super().__init__(person_id, name, address)

        self.Password = "password"
