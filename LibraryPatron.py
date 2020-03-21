class LibraryPatron(object):
    def __init__(self, name):
        self.name = name
        self.booksCheckedOut = []
        
    def checkOutBook(self, checkOutLimit, Book):
        if len(self.booksCheckedOut) >= checkOutLimit:
            print("Sorry", self.name, "you've reached the limit of", self.checkOutLimit,"books")
        else:
            self.booksCheckedOut.append(Book)
            print(self.name,"has checked out", Book)
            
    def returnBook(self, Book):
        self.booksCheckedOut.remove(Book.title)
        print(self.name,"has returned", Book.title)
        
    def printCheckedOutBooks(self):
        print(self.name,"has the following books checked out:")
        for i in self.booksCheckedOut:
            print("\t", i)

class AdultPatron(LibraryPatron):
    def __init__(self,name):
        LibraryPatron.__init__(self, name)
        self.checkOutLimit = 4 
        
    def checkOutBook(self, Book):
        LibraryPatron.checkOutBook(self, self.checkOutLimit, Book.title)


class JuvenilePatron(LibraryPatron):
    def __init__(self,name):
        LibraryPatron.__init__(self,name)
        self.checkOutLimit = 2
        
    def checkOutBook(self, Book):
        if not Book.bookType == "Juvenile":
            print("Sorry", self.name, Book.title, "is an adult book")
        else:
            LibraryPatron.checkOutBook(self, self.checkOutLimit, Book.title)
