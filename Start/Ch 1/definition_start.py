# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class book:
    def __init__(self, author, price):
        self.author=author
        self.price=price

    def geprice(self):
        if hasattr(self, "_discount" ):
            price=self.price-(self.price*self._discount)
            return price
        else:
         return self.price
    
    def setdiscount(self, amount):
        self._discount=amount



# TODO: create instances of the class
book1=book("ken Miles", 200)
book2=book("eudis Muhangi", 23)

# TODO: print the class and property
print(book1.geprice())
book1.setdiscount(0.35)
print(book1.geprice())
print(book1.author)