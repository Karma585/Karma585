# Initialize empty lists, set, and dictionary
book_list = []
author_set = set()
books_dict = {}

# Add books
book_list.append("Python Programing")
author_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

book_list.append("Data structures and algorithms")
author_set.add("Jane Doe")
books_dict["Data structures anf Algorithms"] = "Jane Doe"

book_list.append("Machine Learning Basics")
author_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

#search for a book
search_title = input("Enter the title of the book")
if search_title in book_list:
    print(f"Book found! Author:{books_dict[search_title]}")
else:
    print("Book not founnd")

# Display all books
    print("list of Books:")
    for book in book_list:
        print(book)

 # Remove a book
        remove_title = input("Enter the title of the book to remove or else enter to skip")
        if remove_title in book_list:
            romove_author = books_dict[remove_title]
            book_list.remove(remove_title)
            author_set.remove(remove_title)
            del books_dict[remove_title]
            print("Book removed successfully")
            print("Books Available; ", book_list)

        else:
            print("Book not found")