# Hier moet een frontend view komen van de catalog, deze moet alle informatie vanuit classes in halen

from Repository import BooksRepository
from Objects.BookObject import Book

class Catalog:
    def __init__(self):
        self.AllBooksList = []
        allBooks = BooksRepository.readJson()
        for singleBook in allBooks:
            self.AllBooksList.append(Book(singleBook))

    def ViewCatalog(self, searchTerm = ""):
        if searchTerm != "":
            AllBooksView = list(filter(lambda x: searchTerm in x.Id+x.Title+x.Author+x.Genre, self.AllBooksList))
        else:            
            AllBooksView = self.AllBooksList

        bookRowView = ""
        whiteSpaceToAddTitle, whiteSpaceToAddAuthor, whiteSpaceToAddGenre = 0, 0, 0

        for book in AllBooksView:
            if len(book.Title) > whiteSpaceToAddTitle:
                whiteSpaceToAddTitle = len(book.Title)
            if len(book.Author) > whiteSpaceToAddAuthor:
                whiteSpaceToAddAuthor = len(book.Author)
            if len(book.Genre) > whiteSpaceToAddGenre:
                whiteSpaceToAddGenre = len(book.Genre)

        for book in AllBooksView:
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
                                                                                         " "*(whiteSpaceToAddGenre-6))

        print("="*len(columnTitleFormatting))
        print(columnTitleFormatting)
        print(bookRowView[:-1])
        print("="*len(columnTitleFormatting))

    def searchBook(self):
        searchTerm = input("Voer een zoekterm in (op id, auteur, titel of genre): ")
        Catalog.ViewCatalog(self, searchTerm)