

from Repository import LoanedBooksRepository

class LoanedBook:
    def __init__(self, book_id):
        book = LoanedBooksRepository.getLoanedBookId(book_id)        
        self.Id = book_id
        self.Id_book = book['id_book']
        self.Id_subscriber = book['id_subscriber']
        self.Returned = book['returned']
        self.DateRented = book['dateRented']
        self.DateReturned = book['dateReturned']

    @staticmethod
    def AddLoanedBook(id_book,  id_subscriber):
        loanedBookToAdd = { "id_book" : id_book, "id_subscriber" : id_subscriber, "returned" : False,"dateRented": dt.date.today() }
        newLoanedBookId = LoanedBooksRepository.addBookToJsonAndReturnId(loanedBookToAdd)     
        print(newLoanedBookId)

        return LoanedBook(newLoanedBookId)

    @staticmethod
    def ReturnLoanedBook(id_book,id_subscriber):
        loanedBookToReturn = { "id_book" : id_book, "id_subscriber" : id_subscriber, "returned" : True,"dateReturned": dt.date.today() }
        succesIndicator = LoanedBooksRepository.returnBook(loanedBookToReturn)
        print(succesIndicator)
        return LoanedBook(succesIndicator)


        