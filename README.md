<h1 align="center">
  📚 LIBRARY MANAGEMENT SYSTEM
</h1>

<h3 align="center">
  A Python Object-Oriented Programming Project
</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Status-Completed-success" />
<img src="https://img.shields.io/badge/Concepts-OOP-orange" />
<img src="https://img.shields.io/badge/Editor-VS%20Code-blue?logo=visualstudiocode" />
</p>

📖 About The Project

The Library Management System is a Python-based application designed to manage a campus library that lends three types of items:

📕 Books
📰 Magazines
📀 DVDs

The program allows library members to borrow and return items, checks item availability, enforces borrowing limits, calculates late fees, and handles invalid operations using exceptions.

This project demonstrates important Object-Oriented Programming (OOP) concepts in Python.

✨ Features
📚 Manage Books, Magazines, and DVDs.
👤 Create and manage library members.
📥 Borrow available library items.
📤 Return borrowed items.
🔒 Encapsulation using private attributes.
🧬 Inheritance through an abstract parent class.
🔄 Polymorphism for different late fee calculations.
⚠️ Exception handling using ValueError.
📊 Track the total number of library items.
🧾 Generate readable descriptions of items.
💰 Late Fee Structure
Library Item	Late Fee Per Day
📕 Book	Rs 2
📰 Magazine	Rs 1
📀 DVD	Rs 5

Example: For 3 days late:

Book = Rs 6
Magazine = Rs 3
DVD = Rs 15
🛠️ Technologies Used
Technology	Purpose
Python 3.12+	Programming language
VS Code	Code editor
Git	Version control
GitHub	Project hosting
📂 Project Structure
text
Library_Manager/
│
├── main.py          # Main program and demonstration
├── models.py        # Classes and OOP implementation
├── README.md        # Project documentation
├── output.txt       # Final program output
└── .gitignore       # Ignored files

🧠 OOP Concepts Implemented
Concept	Implementation
Abstraction	LibraryItem abstract class
Inheritance	Book, Magazine, DVD
Encapsulation	__available, __borrowed
Polymorphism	Different late_fee() implementations
Exception Handling	ValueError
🚀 How to Run the Project
1. Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/library-manager.git

2. Open the Project Folder
bash
cd library-manager

3. Run the Application
bash
python main.py


Note: Python 3.12 or later is required. No external packages are needed.

🖥️ Sample Output
text
========== LIBRARY MANAGEMENT SYSTEM ==========

--- Borrowing Items ---
Alice borrowed: Book: Python 101 by A. Rao (ID 1)
Could not borrow: Python 101 is already borrowed.

--- Borrowing Limit Test ---
Bob borrowed: DVD: Python Tutorial, Duration 120 minutes (ID 3)
Borrowing error: Bob has reached the borrowing limit.

--- Invalid Return Test ---
Return error: Tech Today was not borrowed by Bob.

--- Late Fee Calculation ---
Book -> Late fee for 3 days: Rs 6
Magazine -> Late fee for 3 days: Rs 3
DVD -> Late fee for 3 days: Rs 15

--- Total Items ---
Total items created: 3

========== PROGRAM FINISHED ==========


For the complete console output, see output.txt.

📝 Assignment Reflection
1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is abstract because it provides common features to all library items but should not be directly instantiated. Every child class must implement its own late_fee() method. If DVD does not implement this abstract method, Python raises a TypeError when we try to create a DVD object.

2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Accessing item.__available from outside the class raises an AttributeError because Python uses name mangling for double-underscore attributes. We use is_available() to check availability safely without directly accessing the private variable.

3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared by all objects of the LibraryItem hierarchy, and it keeps track of the total number of items created. On the other hand, self.title is an instance attribute, meaning every individual item has its own title.

📌 Learning Outcomes

Through this project, I learned how to:

Design classes using Object-Oriented Programming.
Implement abstraction, inheritance, encapsulation, and polymorphism.
Handle invalid operations using exceptions.
Work with private attributes and class attributes.
Organize Python projects into multiple files.
Use Git and GitHub for version control.


<p align="center">
⭐ <b>Thank you for visiting this project!</b> ⭐
</p>
