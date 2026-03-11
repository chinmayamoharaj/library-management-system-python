# library-management-system-python
A Python-based Library Management System using Python and MySQL that allows you to manage books and students efficiently.
It includes book management, student management, book issue and return, and a MySQL database integration.

# Features
  - Add, view, update, and delete books
  - Add and view students
  - Issue and return books
  - Search for books and students
  - View all issued books
  - Menu-driven interface
  - MySQL database integration

# Requirements
   - Python 3.13
   - MySQL database installed
   - `mysql-connector-python` library

# Command Prompt
pip install mysql-connector-python

#Installation
1. Clone this repository.
2. Go to the project folder.
3. Install dependencies.
4. Make sure MySQL is running and create the database.

# How to create database in MySQL

CREATE DATABASE library_db;
USE library_db;
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    quantity INT
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    course VARCHAR(255)
);

CREATE TABLE issue_book (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    book_id INT,
    issue_date DATE,
    return_date DATE,
    FOREIGN KEY(student_id) REFERENCES students(student_id),
    FOREIGN KEY(book_id) REFERENCES books(book_id)
);
# How to use the program
 
2. Enter your MySQL password when prompted.

3. You will see a menu with the following options:
- Add Book
- View Books
- Update Book Quantity
- Delete Book
- Add Student
- View Students
- Issue Book
- Return Book
- Search Book
- Search Student
- View Issued Books
- Exit

4. Follow the prompts to perform library operations.
5. 
#Author
  Chinmaya Moharaj  
  [GitHub Profile](https://github.com/chinmayamoharaj)
