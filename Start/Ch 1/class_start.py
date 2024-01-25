# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES=("EBOOK", "PAPERCOPY", "HARDCOVER")

    # TODO: double-underscore properties are hidden from other classes
    __booklist=None


    # TODO: create a class method
    @classmethod
    def get_book_types(cls): #take class argument instead of self
        return cls.BOOK_TYPES

    # TODO: create a static method
    def getbooklist():
        if Book.__booklist==None:
            Book.__booklist=[]
        return Book.__booklist
         

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title):
        self.title = title


# TODO: access the class attribute
print("class method that prints book types:", Book.get_book_types()) #acces them using a class its self

# TODO: Create some book instances
b1=Book("all things fall apart")


# TODO: Use the static method to access a singleton object

thebooks=Book.getbooklist()
thebooks.append(b1)
print(thebooks)