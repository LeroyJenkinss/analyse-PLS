# Maak hier een class aan die op basis van een Id een Book informatie inlaadt vanuit de repository
# Zo moeten de attributen worden gevuld op basis van de repository methodes. Hartstikke leuk en aardig maar de andere classes moeten ook gebouwd worden
# Waaronder LoanItem. Let wel op dat het aansluit op de class diagram, dus ook dat de associaties klopt.
# Zo moet bijv BookItem class wel de book titel trekken van de Book class. De book class trekt dan informatie van de Repository/BooksRepository
# 
# Ik verwacht geen vragen! Anders krijgen jullie allemaal bakka's!
# nee grapje
# als ik weer is onduidelijk ben hoor ik het wel mijn kinderen

from Repository import BooksRepository

class Book:
    def __init__(self, book_id):
        book = BooksRepository.getBook(book_id)        
        self.Id = book_id
        self.BookItems = book['bookItems']
        self.Title = book['title']
        self.Author = book['author']
        self.Genre = book['genre']

    @staticmethod
    def AddBook(bookItems,  title, author, genre):
        bookToAdd = { "bookItems" : bookItems, "title" : title, "author" : author,"genre": genre }
        newBookId = BooksRepository.addBookToJsonAndReturnId(bookToAdd)     
        print(newBookId)

        return Book(newBookId)

    @staticmethod
    def RemoveBook(book_id):
        BooksRepository.removebook(book_id)
        # Tarik:
        # Hier nog wat code die naar een nieuwe methode in de bookrepository gaat wat het book op basis van de bookId verwijdert uit het Json bestandje. 
