

from Repository import LoanedBooksRepository
import datetime as dt

class LoanedBook:
    def __init__(self, loanedBook_id):
        book = LoanedBooksRepository.getLoanedBook(loanedBook_id)
        
        if isinstance(loanedBook_id, str):
            loanedBook_id = int(loanedBook_id)        
        self.Id = loanedBook_id
        self.Id_book = book['id_book']
        self.Id_subscriber = book['id_subscriber']
        self.Returned = book['returned']
        self.DateRented = book['dateRented']
        self.DateReturned = book['dateReturned']

    @staticmethod
    def AddLoanedBook(id_book,  id_subscriber):
        loanedBookToAdd = { "id_book" : id_book, "id_subscriber" : id_subscriber, "returned" : False, "dateRented": str(dt.datetime.now()), "dateReturned": ""}
        newLoanedBookId = LoanedBooksRepository.addBookToJsonAndReturnId(loanedBookToAdd)     

        return LoanedBook(newLoanedBookId)

    def ReturnLoanedBook(self):
        self.Returned = True
        self.DateReturned = str(dt.datetime.now())
        loanedBookToReturn = { "id_book" : self.Id_book, "id_subscriber" : self.Id_subscriber, "returned" : True, "dateRented": self.DateRented, "dateReturned": self.DateReturned}
        LoanedBooksRepository.returnBook(self.Id, loanedBookToReturn)

        return self