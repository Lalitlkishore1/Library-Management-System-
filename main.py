books = []

def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    books.append({
        "id": book_id,
        "name": name,
        "issued": False,
        "student": "",
        "days": 0
    })
    print("Book added successfully!")

def view_books():
    if len(books) == 0:
        print("No books available.")
        return
    print("\nLibrary Books")
    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print(book["id"], "-", book["name"], "-", status)

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                print("Book already issued.")
                return
            student = input("Enter student name: ")
            days = int(input("Enter number of days issued: "))
            book["issued"] = True
            book["student"] = student
            book["days"] = days
            print("Book issued successfully!")
            return
    print("Book not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["id"] == book_id:
            if not book["issued"]:
                print("Book was not issued.")
                return
            extra_days = int(input("Enter late days (0 if none): "))
            fine = extra_days * 10
            book["issued"] = False
            book["student"] = ""
            book["days"] = 0
            print("Book returned successfully!")
            if fine > 0:
                print("Fine to pay: Rs.", fine)
            return
    print("Book not found.")

def search_book():
    name = input("Enter book name to search: ")
    for book in books:
        if book["name"].lower() == name.lower():
            status = "Issued" if book["issued"] else "Available"
            print("\nBook Found")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Status:", status)
            if book["issued"]:
                print("Issued to:", book["student"])
            return
    print("Book not found.")

while True:
    print("\n----- Library Management System -----")
    print("1 Add Book")
    print("2 View Books")
    print("3 Issue Book")
    print("4 Return Book")
    print("5 Search Book")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        print("Exiting system")
        break
    else:
        print("Invalid choice")
