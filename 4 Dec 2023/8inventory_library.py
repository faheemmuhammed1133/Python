# library management
books=["Alchemist","Chemistry","Physics","Maths","Atomic Habits"]
# print(len(books))
while True:
    print('\nLibrary Management System')
    print('1. Add a book')
    print('2. Display all books')
    print('3. Search for a book by title')
    print('4. Exit')

    y = input('Enter your choice (1-4): ')

    if y == '1':    
        book = input('Enter the title of the book: ')
        books.append(book)
        print(" ")
        print(f'Book "{book}" added successfully.')
    elif y=="2":
        if not books:
            print('No books in the library.')
        else:
            print('List of books in the library:')
            print(books)
    elif y=="3":
        book = input('Enter the title of the book to search: ')
        for i in range(len(books)):
            k="No books named",book,"found in library "
            if book==books[i]:
                print(" ")
                print(books[i])
                j="printed"
                break
        if j!="printed":
            print("")
            print(k)
        
    elif y == '4':
        print('Exiting the library management system. Goodbye!')
        break

    else:
        print('Invalid choice. Please enter a number between 1 and 4.')
