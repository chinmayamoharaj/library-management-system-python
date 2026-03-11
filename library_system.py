# library_system.py
# This includes:-
# -Books management (Add, View, Update, Delete)
# -Students management (Add, View)
# -Issue and Return Books
# -Menu-driven interface
# -MySQL database integration

import mysql.connector
from datetime import date

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter database password: "),  # MySQL password
    database="library_db"
)
cursor = db.cursor()
print("Connected to database!")


# BOOKS

def add_book(title, author, quantity):
    query = "INSERT INTO books (title, author, quantity) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, author, quantity))
    db.commit()
    print("Book added successfully!")


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\nBook ID | Title | Author | Quantity")
    print("--------------------------------------")

    for book in books:
        print(f"{book[0]} | {book[1]} | {book[2]} | {book[3]}")

def search_book():
    title = input("Enter book title to search: ")
    query = "SELECT * FROM books WHERE title LIKE %s"
    cursor.execute(query, ('%' + title + '%',))
    result = cursor.fetchall()

    if result:
        for book in result:
            print(book)
    else:
        print("Book not found!")

def view_issued_books():
        query = """
        SELECT issue_book.issue_id, students.name, books.title, issue_book.issue_date, issue_book.return_date
        FROM issue_book
        JOIN students ON issue_book.student_id = students.student_id
        JOIN books ON issue_book.book_id = books.book_id
        """

        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)

def update_book(book_id, quantity):
    query = "UPDATE books SET quantity=%s WHERE book_id=%s"
    cursor.execute(query, (quantity, book_id))
    db.commit()
    print("Book updated successfully!")


def delete_book(book_id):

    cursor.execute("SELECT * FROM issue_book WHERE book_id=%s AND return_date IS NULL", (book_id,))
    issued = cursor.fetchone()

    if issued:
        print("Book cannot be deleted. It is currently issued.")
        return

    query = "DELETE FROM books WHERE book_id=%s"
    cursor.execute(query, (book_id,))
    db.commit()

    print("Book deleted successfully!")

#  STUDENTS

def add_student(name, course):
    query = "INSERT INTO students (name, course) VALUES (%s, %s)"
    cursor.execute(query, (name, course))
    db.commit()
    print("Student added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    for student in cursor.fetchall():
        print(student)

def search_student():
    name = input("Enter student name: ")
    query = "SELECT * FROM students WHERE name LIKE %s"
    cursor.execute(query, ('%' + name + '%',))
    result = cursor.fetchall()

    if result:
        for student in result:
            print(student)
    else:
        print("Student not found!")

#  ISSUE / RETURN

def issue_book(student_id, book_id):
    issue_date = date.today()
    cursor.execute("SELECT quantity FROM books WHERE book_id=%s", (book_id,))
    result = cursor.fetchone()
    if result is None:
        print("Book ID not found!")
        return
    qty = result[0]
    if qty > 0:
        cursor.execute("INSERT INTO issue_book (student_id, book_id, issue_date) VALUES (%s, %s, %s)",
                       (student_id, book_id, issue_date))
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id=%s", (book_id,))
        db.commit()
        print("Book issued successfully!")
    else:
        print("Book not available!")


def return_book(issue_id):
    return_date = date.today()
    cursor.execute("SELECT book_id FROM issue_book WHERE issue_id=%s", (issue_id,))
    result = cursor.fetchone()
    if result is None:
        print("Issue ID not found!")
        return
    book_id = result[0]
    cursor.execute("UPDATE issue_book SET return_date=%s WHERE issue_id=%s", (return_date, issue_id))
    cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE book_id=%s", (book_id,))
    db.commit()
    print("Book returned successfully!")


# MENU

def menu():
    while True:
        print("\nLibrary Management System")
        print("-------------------------------------")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book Quantity")
        print("4. Delete Book")
        print("5. Add Student")
        print("6. View Students")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Search Book")
        print("10. Search Student")
        print("11. View Issued Books")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            quantity = int(input("Enter quantity: "))
            add_book(title, author, quantity)
        elif choice == '2':
            view_books()
        elif choice == '3':
            book_id = int(input("Enter book ID: "))
            quantity = int(input("Enter new quantity: "))
            update_book(book_id, quantity)
        elif choice == '4':
            book_id = int(input("Enter book ID: "))
            delete_book(book_id)
        elif choice == '5':
            name = input("Enter student name: ")
            course = input("Enter course: ")
            add_student(name, course)
        elif choice == '6':
            view_students()
        elif choice == '7':
            student_id = int(input("Enter student ID: "))
            book_id = int(input("Enter book ID: "))
            issue_book(student_id, book_id)
        elif choice == '8':
            issue_id = int(input("Enter issue ID: "))
            return_book(issue_id)
        elif choice == '9':
            search_book()
        elif choice == '10':
            search_student()
        elif choice == '11':
            view_issued_books()
        elif choice == '12':
            print("Thanks for using Chinmaya's Program...")
            break
        else:
            print("Invalid choice....... Try again !!!")


# Now you can run the program
menu()