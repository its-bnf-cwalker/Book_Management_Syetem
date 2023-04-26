#Creating class of book for storing title and author

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class BookManager:
    def __init__(self):
        self.books = [] #List of books

    def add_book(self, title, author): #function of adding book
        book = Book(title, author) #creating an instance of class book by passing two arguments
        self.books.append(book) #appending book in self.book list created
        print("Book added successfully.")

    def remove_book(self, title): #function of removing book
        for book in self.books: #Iterating through all book in the list
            if book.title == title: #if book is present then go ahead otherwise end the program
                self.books.remove(book) #list provide remove method to remove element from list with the help of that we successfully remove the book
                print("Book removed successfully.")
                return
        print("Book not found.")

    def display_books(self): #function of displaying book
        if not self.books: #if book is not present print no book found
            print("No books found.")
        else: #if present then print Books in the system along with al the books in the list
            print("Books in the system:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}")

    def search_book(self, title): #function of searching book with title parameter
        found = False
        for book in self.books: #Iterating through all book in the list
            if book.title == title: # If boo with title is present in the list then print the title and author name
                print(f"Title: {book.title}, Author: {book.author}")
                found = True
        if not found: # if not present then then print book not found
            print("Book not found.")


def main():
    book_manager = BookManager() #Storing Object instance of book manager in variable
    while True:  #Running infinity loop
        print("Welcome to the Book Management System!")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Search Book")
        print("5. Exit")
        choice = input("Enter your choice: ") #Based on the data provided user will choose an option and it will store in variable choice 
        #The condition will execute based on the data variable choice
        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book_manager.add_book(title, author) #Utilizing the function which was create in Book_Manager class and passing two argument to add the book in list

        elif choice == '2':
            title = input("Enter the title of the book to be removed: ")
            book_manager.remove_book(title)

        elif choice == '3':
            book_manager.display_books()

        elif choice == '4':
            title = input("Enter the title of the book to be searched: ")
            book_manager.search_book(title)

        elif choice == '5':
            print("Thank you for using the Book Management System!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == '__main__': #It will execute first since the condition is true
    main() # the main function is called
    
