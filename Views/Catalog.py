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
        bookRowView = ""
        whiteSpaceToAddTitle, whiteSpaceToAddAuthor, whiteSpaceToAddGenre = 0, 0, 0

        for book in self.AllBooksList:
            if len(book.Title) > whiteSpaceToAddTitle:
                whiteSpaceToAddTitle = len(book.Title)
            if len(book.Author) > whiteSpaceToAddAuthor:
                whiteSpaceToAddAuthor = len(book.Author)
            if len(book.Genre) > whiteSpaceToAddGenre:
                whiteSpaceToAddGenre = len(book.Genre)

        for book in self.AllBooksList:
            if int(book.Id) > 9:
                whiteSpaceAfterId = " "*6
            else:
                whiteSpaceAfterId = " "*7
                
            whiteSpaceAfterTitle = (" " * (whiteSpaceToAddTitle-len(book.Title)))
            whiteSpaceAfterAuthor = (" " * (whiteSpaceToAddAuthor-len(book.Author)))
            whiteSpaceAfterGenre = (" " * (whiteSpaceToAddAuthor-len(book.Genre)))

            bookRowView += "|| {}{}|| {}{}|| {}{}|| {}{}||\n".format(book.Id, whiteSpaceAfterId, 
                                                                     book.Title, whiteSpaceAfterTitle, 
                                                                     book.Author, whiteSpaceAfterAuthor, 
                                                                     book.Genre, whiteSpaceAfterGenre)
        
        columnTitleFormatting = "|| BookId: || Title:{}|| Author:{}|| Genre:{}||".format(" "*(whiteSpaceToAddTitle-6),
                                                                                         " "*(whiteSpaceToAddAuthor-7),
                                                                                         " "*(whiteSpaceToAddGenre-4))

        print("="*len(columnTitleFormatting))
        print(columnTitleFormatting)
        print(bookRowView[:-1])
        print("="*len(columnTitleFormatting))

Catalog().ViewCatalog()
