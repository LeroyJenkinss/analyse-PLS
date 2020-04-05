# Hier moet een frontend view komen van de catalog, deze moet alle informatie vanuit classes in halen

from Repository import BooksRepository
from Objects.BookObject import Book

class Catalog:
    def __init__(self):
        self.AllBooksList = []
        allBooks = BooksRepository.readJson()
        for singleBook in allBooks:
            self.AllBooksList.append(Book(singleBook)) 

    def ViewCatalog(self):
        self.__init__()
        for book in self.AllBooksList:
            print(book.Title)

Catalog().ViewCatalog()
