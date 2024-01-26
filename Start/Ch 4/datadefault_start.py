# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str="Tears of the sun"
    author: str="Max Game"
    pages: int=20
    price: float=3.5
b1=Book()
print(b1)