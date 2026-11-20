# Program 15: Library Management System

books = {}

while True:
    print("\n=== Library Management ===")
    print("1. Add book\n2. View books\n3. Borrow book\n4. Return book\n5. Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        book_id = input("Book ID: ").strip()
        if book_id in books:
            print("Book ID already exists.")
        else:
            title = input("Book title: ").strip()
            books[book_id] = {"title": title, "available": True}
            print("Book added.")
    elif choice == "2":
        if not books:
            print("No books in the library.")
        for book_id, book in books.items():
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book_id}: {book['title']} - {status}")
    elif choice == "3":
        book_id = input("Book ID to borrow: ").strip()
        if book_id not in books:
            print("Book not found.")
        elif not books[book_id]["available"]:
            print("That book is already borrowed.")
        else:
            books[book_id]["available"] = False
            print("Book borrowed.")
    elif choice == "4":
        book_id = input("Book ID to return: ").strip()
        if book_id not in books:
            print("Book not found.")
        elif books[book_id]["available"]:
            print("That book was not marked as borrowed.")
        else:
            books[book_id]["available"] = True
            print("Book returned.")
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
