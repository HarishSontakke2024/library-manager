Library Management System
Project Description

This is a Python-based Library Management System developed using Object-Oriented Programming (OOP) concepts.

The system manages three types of library items:

Books
Magazines
DVDs

Members can borrow and return items. The program checks item availability, enforces borrowing limits, calculates late fees, and handles invalid operations using exceptions.

Features
Abstract parent class LibraryItem.
Child classes Book, Magazine, and DVD.
Different late fees for each item type:
Book: Rs 2 per day.
Magazine: Rs 1 per day.
DVD: Rs 5 per day.
Private item availability and borrowed item lists.
Member borrowing and returning functionality.
Borrowing limit enforcement.
Exception handling using ValueError.
Polymorphism for late fee calculation.
Total item counting using a class attribute.
Project Structure
text
Library_Manager/
│
├── main.py
├── models.py
├── README.md
├── output.txt
└── .gitignore

Technologies Used
Python 3.12+
Visual Studio Code
Git and GitHub
How to Run
Open the project folder in VS Code.
Open the terminal.
Run:
bash
python main.py

Reflection Questions
1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is abstract because it provides common features to all library items but should not be directly instantiated. Every child class must implement its own late_fee() method. If DVD does not implement this abstract method, Python raises a TypeError when we try to create a DVD object.

2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Accessing item.__available from outside the class raises an AttributeError because Python uses name mangling for double-underscore attributes. We use is_available() to check availability safely without directly accessing the private variable.

3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared by all objects of the LibraryItem hierarchy, and it keeps track of the total number of items created. On the other hand, self.title is an instance attribute, meaning every individual item has its own title.

Author

Developed as a Python Object-Oriented Programming assignment.