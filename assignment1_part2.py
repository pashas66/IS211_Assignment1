# Week 1 Assignment - Part 2

#created a class called 'book' and then a function that takes in 2 attributes (title and author). 
class Book: 
# a function that takes in an author and a title, and sets them to the object variables.
    def __init__(self, title="", author="" ): #initialized the author and title to the blank string
         self.author = author
         self.title = title

#A function called display, which when called, simply prints out a string representing the book
    def display(self):
         print(self.title + ", written by " + self.author)

#Instantiate two objects from this class and then print them by calling the display functon 
book1 = Book("Of Mice and Men", "John Steinbeck")
book1.display()

book2 = Book("To Kill a Mockingbird", "Harper Lee")
book2.display()

