import LibraryBook as lb
import LibraryPatron as lp

def main():
    book1 = lb.Book("Alice in Wonderland", "Juvenile")
    book2 = lb.Book("The Cat in the Hat", "Juvenile")
    book3 = lb.Book("Harry Potter and the Sorcerer's Stone", "Juvenile")
    book4 = lb.Book("The Hobbit", "Juvenile")
    book5 = lb.Book("The Da Vinci Code", "Adult")
    book6 = lb.Book("The Girl with the Dragon Tattoo", "Adult")
    
    patron1 = lp.JuvenilePatron("Jimmy")
    patron2 = lp.AdultPatron("Sophia")

    patron1.checkOutBook(book6)
    patron1.checkOutBook(book1)
    patron1.checkOutBook(book2)
    patron1.printCheckedOutBooks()
    patron1.checkOutBook(book3)
    patron1.returnBook(book1)
    patron1.checkOutBook(book3)
    patron1.printCheckedOutBooks()
    patron2.checkOutBook(book5)
    patron2.checkOutBook(book4)
    patron2.printCheckedOutBooks()

if __name__ == "__main__":
    main()

