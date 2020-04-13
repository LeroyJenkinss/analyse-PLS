from Repository import BooksRepository

class Book:
    def __init__(self, book_id):
        book = BooksRepository.getBook(book_id)        

        if isinstance(book_id, str):
            book_id = int(book_id)
        self.Id = book_id
        self.BookItems = book['bookItems']
        self.Title = book['title']
        self.Author = book['author']
        self.Genre = book['genre']

    @staticmethod
    def AddBook(bookItems,  title, author, genre):
        bookToAdd = { "bookItems" : bookItems, "title" : title, "author" : author,"genre": genre }
        newBookId = BooksRepository.addBookToJsonAndReturnId(bookToAdd)     

        return Book(newBookId)

    def RemoveBook(self):
        BooksRepository.removebook(self.Id)