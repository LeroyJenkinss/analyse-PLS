# Hier moet een frontend view komen van de catalog, deze moet alle informatie vanuit classes in halen
import os
from Repository import BooksRepository, LoanedBooksRepository, SubscribersRepository
from Objects.BookObject import Book
from Objects.LoanBooksObject import LoanedBook
from Objects.SubscriberObject import Subscriber

class LoanAdministration:
    def __init__(self):
        self.AllLoanedBooksList = []
        self.AllSubscribersList = []
        allLoanedBooks = LoanedBooksRepository.readJson()
        allSubscribers = SubscribersRepository.readJson()
        for singleLoanedBook in allLoanedBooks:
            loanObject = LoanedBook(singleLoanedBook)
            self.AllLoanedBooksList.append(loanObject)
        for subscriber in allSubscribers:
            subscriberObject = Subscriber(subscriber)
            self.AllSubscribersList.append(subscriberObject)

    def ViewLoanAdministration(self, searchTerm = ""):
        if searchTerm != "":
            AllBooksView = list(filter(lambda x: searchTerm.lower() in (str(x.Id)+Book(x.Id_book).Title+Subscriber(x.Id_subscriber).Name+str(x.Returned)+x.DateRented+x.DateReturned).lower(), self.AllLoanedBooksList))
        else:            
            AllBooksView = self.AllLoanedBooksList

        bookRowView = ""
        whiteSpaceToAddTitle, whiteSpaceToAddSubscriberName, whiteSpaceToAddDateRented, whiteSpaceToAddDateReturned = 0, 0, 0, 0

        for book in AllBooksView:
            bookObject = Book(book.Id_book)
            subscriberObject = Subscriber(book.Id_subscriber)
            if len(bookObject.Title) > whiteSpaceToAddTitle:
                whiteSpaceToAddTitle = len(bookObject.Title)
            if len(subscriberObject.Name) > whiteSpaceToAddSubscriberName:
                whiteSpaceToAddSubscriberName = len(subscriberObject.Name)
            if len(book.DateRented) > whiteSpaceToAddDateRented:
                whiteSpaceToAddDateRented = len(book.DateRented)
            if len(book.DateReturned) > whiteSpaceToAddDateReturned:
                 whiteSpaceToAddDateReturned = len(book.DateReturned)

        for book in AllBooksView:
            bookObject = Book(book.Id_book)
            subscriberObject = Subscriber(book.Id_subscriber)
            if int(book.Id) > 9:
                whiteSpaceAfterId = " "*6
            else:
                whiteSpaceAfterId = " "*7
                
            whiteSpaceAfterTitle = (" " * (whiteSpaceToAddTitle-len(bookObject.Title)))
            whiteSpaceAfterSubscriberName = (" " * (whiteSpaceToAddSubscriberName-len(subscriberObject.Name)))
            whiteSpaceAfterDateRented = (" " * (whiteSpaceToAddDateRented-len(book.DateRented)))
            whiteSpaceAfterDateReturned = (" " * (whiteSpaceToAddDateReturned-len(book.DateReturned)))

            bookRowView += "|| {}{}|| {}{}|| {}{}|| {}{}|| {}{}||\n".format(book.Id, whiteSpaceAfterId, 
                                                                     bookObject.Title, whiteSpaceAfterTitle, 
                                                                     subscriberObject.Name, whiteSpaceAfterSubscriberName, 
                                                                     book.DateRented, whiteSpaceAfterDateRented,
                                                                     book.DateReturned, whiteSpaceAfterDateReturned)
        
        columnTitleFormatting = "|| LoanId: || Book Title:{}|| Rented By:{}|| Date Rented:{}|| Date Returned:{}||".format(" "*(whiteSpaceToAddTitle-11),
                                                                                         " "*(whiteSpaceToAddSubscriberName-10),
                                                                                         " "*(whiteSpaceToAddDateRented-12),
                                                                                         " "*(whiteSpaceToAddDateReturned-14))

        print("="*len(columnTitleFormatting))
        print(columnTitleFormatting)
        print(bookRowView[:-1])
        print("="*len(columnTitleFormatting))

    def SearchBook(self):
        searchTerm = input("Voer een zoekterm in (op id, auteur, titel of genre): ")
        LoanAdministration.ViewLoanAdministration(self, searchTerm)

    def AddSubscriber(self, name, adress):
        newSubscriber = Subscriber.AddSubscriber(name, adress)
        self.AllSubscribersList.append(newSubscriber)

    def LoanBook(self, id_book, id_subscriber):
        newLoanedBook = LoanedBook.AddLoanedBook(id_book, id_subscriber)
        self.AllLoanedBooksList.append(newLoanedBook)

    def ReturnBook(self, id_loan):
        returnedLoanItem = LoanedBook(id_loan).ReturnLoanedBook()
        self.AllLoanedBooksList.append(returnedLoanItem)