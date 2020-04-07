# Hier moet een frontend view komen van de catalog, deze moet alle informatie vanuit classes in halen
import os
from Repository import BooksRepository, LoanedBooksRepository, SubscribersRepository
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

    def SearchBook(self):
        searchTerm = input("Voer een zoekterm in (op id, auteur, titel of genre): ")
        Catalog.ViewCatalog(self, searchTerm)

    def MakeBackup(self):
        BooksRepository.createBackup()
        LoanedBooksRepository.createBackup() 
        SubscribersRepository.createBackup()

    def RecoverBackup(self):
        listOfDirectoryBackups = next(os.walk("Data/Backup"))[1]
        dictOfDirectoryBackups = dict(enumerate(listOfDirectoryBackups, start=1))
        for directory in dictOfDirectoryBackups:
            print("{} : {}".format(directory, dictOfDirectoryBackups[directory]))
        backupToRecoverIndex = int(input("Welk backup wil je herstellen? (geef nummer op van backup): ").strip())

        if backupToRecoverIndex in dictOfDirectoryBackups:            
            BooksRepository.recoverBackup(dictOfDirectoryBackups[backupToRecoverIndex])
            LoanedBooksRepository.recoverBackup(dictOfDirectoryBackups[backupToRecoverIndex]) 
            SubscribersRepository.recoverBackup(dictOfDirectoryBackups[backupToRecoverIndex])
            print("Backup succesvol hersteld")
        else:
            print(backupToRecoverIndex)
            print("Backup bestaat niet! Kies een andere index")

Catalog().RecoverBackup()