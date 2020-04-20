from Views.Catalog import Catalog
from Views.LoanAdministration import LoanAdministration
from Objects.BookObject import Book
from Objects.LoanBooksObject import LoanedBook
from Objects.SubscriberObject import Subscriber
from Objects.LibrarianObject import Librarian
from Repository import SubscribersRepository

print("Welkom bij deze super coole Public Library System" )
print("Aan de hand van de cijfers kan je navigeren, door de cijfer in te tikken en op enter te drukken" )

def inputOnInteger(textToDisplay):
     userInput = input(textToDisplay)
     try:
          convertedInput = int(userInput)
          return convertedInput
     except ValueError:
          print("Input should be a whole number (int)")
          inputOnInteger(textToDisplay)

def startApplication(stopApplication = False, loggedInAsLibrarian = False):
     catalogView = Catalog()
     loanAdministrationView = LoanAdministration()

     while stopApplication == False:
          print("\n1.  Laat Catalogus zien (Niet uitgeleende boeken) 2.  Zoek in Catalogus" )
          print("3.  Laat LoanAdministration zien                  4.  Zoek in LoanAdministration" )
          print("5.  Laat Subscribers / Customers zien             6.  Nieuw Subscriber/Customer toevoegen" )
          print("7.  Leen Boek uit                                 8.  Boek Terugbrengen" )
          print("9.  Nieuw boek toevoegen                          10. Backup maken" )
          print("11. Backup herstellen                             12. Sluit af" )

          inputUser = input("Keuze: ")

          if inputUser == "1":
               catalogView.ViewCatalog()
          elif inputUser == "2":
               catalogView.SearchBook()
          elif inputUser == "3":
               loanAdministrationView.ViewLoanAdministration()
          elif inputUser == "4":
               loanAdministrationView.SearchBook()
          elif inputUser == "5":
               for subscriber in loanAdministrationView.AllSubscribersList:
                    print("\nId: {}\nName: {}\nAdres: {}".format(subscriber.Id, subscriber.Name, subscriber.Address))
          elif inputUser == "6":
               print("\nVoeg nieuwe customer / subscriber toe\n")
               name = input("Naam: ")     
               adress = input("Adres: ")     

               loanAdministrationView.AddSubscriber(name, adress)
          elif inputUser == "7":
               id_book = inputOnInteger("\nVoer Id van de book in om uit te lenen: ")
               id_subscriber = inputOnInteger("Voer Id van de customer / subcriber aan om uit te lenen: ")
               try:
                    bookNotAvailable = True
                    bookToLend = Book(id_book)
                    Subscriber(id_subscriber)
                    for book in catalogView.AllBooksList:
                         if book.Id == bookToLend.Id:
                              bookNotAvailable = False

                    if bookNotAvailable != True:
                         loanAdministrationView.LoanBook(id_book, id_subscriber)
                         print("\nBoek is bij deze uitgeleend\n")
                         catalogView.__init__()
                    else:
                         print("Geen beschikbare exemplaren")
               except:
                    print("Geen geldige subscriber id of boek id")  
          elif inputUser == "8":
               loanId = inputOnInteger("\nVoer LoanId in: ")
               try:
                    loanAdministrationView.ReturnBook(loanId)
                    print("\nSuccesvol teruggebracht")
               except:
                    print("Geen valide LoanId")                    
          elif inputUser == "9":
               print("\nEen nieuw boek toevoegen:\n")
               bookTitle = input("Title: ")     
               bookAuthor = input("Author: ")     
               bookGenre = input("Genre: ")     
               bookItems = inputOnInteger("Available books: ")

               catalogView.AddBook(bookItems, bookTitle, bookAuthor, bookGenre)                  
          elif inputUser == "10":
               catalogView.MakeBackup()
          elif inputUser == "11":
               catalogView.RecoverBackup()
          elif inputUser == "12":
               stopApplication = True

     if stopApplication == False:
          startApplication(stopApplication, loggedInAsLibrarian)

startApplication()