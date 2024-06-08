# Write a program which contains one class named as BookStore.
# BookStore class contains two instance variables as Name ,Author.
#That class contains one class variable as NoOfBooks which is initialise to 0.
# There is one instance method of class as Display which displays name, Author
# and number of books.
# Initialise instance variable in init method by accepting values from user as name and author
# Inside init method increment value of NoOfBooks by one.

#After creating the class create two objects of BookStore class as
# Obj1 = BookStore("Linus System Programming","Robert Love")
# Obj1.Display()      #Linus System Programming by Robert Love. No of books: 1

# Obj2 = BookStore("C Programming","Dennis Richie")
# Obj2.Display()      # C Programming by Dennis Richie. No of books: 2

class BookStore:
    NoOfBooks = 0

    def __init__(self, A, B):
        self.Name = A
        self.Author = B

    def Display(self):
        BookStore.NoOfBooks += 1
        print(self.Name+" by "+self.Author+"."+" No of books:",BookStore.NoOfBooks)
        

Obj1 = BookStore("Linus System Programming","Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming","Dennis Richie")
Obj2.Display()


