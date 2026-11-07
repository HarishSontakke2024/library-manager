
<h1 align="center">📚 LIBRARY MANAGEMENT SYSTEM</h1>

<h3 align="center">
  A Python-Based Object-Oriented Programming Project
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OOP-Concepts-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-2ea44f?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Packages-None-blueviolet?style=for-the-badge" />
</p>

<p align="center">
  <b>Manage Library Items • Borrow & Return • Calculate Late Fees • Handle Exceptions</b>
</p>

---

## 📖 About The Project

The **Library Management System** is a Python application developed to manage a campus library that lends three different types of items: Books, Magazines, and DVDs.

The system allows library members to borrow and return items while maintaining item availability, enforcing borrowing limits, calculating late fees, and handling invalid operations through exception handling.

This project is developed using **Object-Oriented Programming (OOP)** principles and demonstrates how Python classes can be used to build a simple, organized, and maintainable application.

---

## ✨ Key Features

- 📚 **Multiple Item Types** – Supports Books, Magazines, and DVDs.
- 👤 **Member Management** – Creates and manages library members.
- 📥 **Borrow Items** – Allows members to borrow available items.
- 📤 **Return Items** – Allows members to return borrowed items.
- 🔒 **Encapsulation** – Protects availability and borrowed item lists using private attributes.
- 🧬 **Inheritance** – Shares common functionality through an abstract parent class.
- 🔄 **Polymorphism** – Calculates late fees differently for each item type.
- ⚠️ **Exception Handling** – Handles invalid borrowing and returning operations safely.
- 📊 **Item Tracking** – Maintains the total number of library items created.

---

## 💰 Late Fee Structure

The library charges different late fees depending on the type of item.

| Library Item | Daily Fee | Fee for 3 Days |
|:---|:---:|:---:|
| 📕 Book | Rs 2/day | **Rs 6** |
| 📰 Magazine | Rs 1/day | **Rs 3** |
| 📀 DVD | Rs 5/day | **Rs 15** |

**Formula:**

`Late Fee = Number of Late Days × Daily Fee`

---

## 🛠️ Technologies Used

| Technology | Purpose |
|:---|:---|
| 🐍 Python 3.12+ | Programming language |
| 💻 Visual Studio Code | Code editor |
| 🔧 Git | Version control |
| 🐙 GitHub | Source code hosting |

**Dependencies:** No external Python packages are required.

---

## 🧠 Object-Oriented Programming Concepts

This project demonstrates the four major OOP principles.

### 1. Abstraction

The `LibraryItem` class is an abstract parent class created using Python's `ABC` module.

It defines common attributes and methods that every library item must follow.

### 2. Inheritance

The following classes inherit from `LibraryItem`:

- `Book`
- `Magazine`
- `DVD`

They reuse common functionality while maintaining their own additional attributes.

### 3. Encapsulation

Private attributes are used to protect important data:

- `__available` – Stores item availability.
- `__borrowed` – Stores a member's borrowed items.

These attributes are accessed and modified through methods rather than directly.

### 4. Polymorphism

Each child class implements its own `late_fee()` method.

The same method call produces different results depending on the item type.

---

## 🏗️ Class Structure

```text
                 LibraryItem (ABC)
                        |
          ┌─────────────┼─────────────┐
          |             |             |
         Book        Magazine        DVD
          |             |             |
          └─────────────┼─────────────┘

                  Member Class
             (Borrowing & Returning)
```

### Class Responsibilities

| Class | Responsibility |
|:---|:---|
| `LibraryItem` | Abstract parent class with common item functionality. |
| `Book` | Manages book details and calculates book late fees. |
| `Magazine` | Manages magazine details and calculates magazine late fees. |
| `DVD` | Manages DVD details and calculates DVD late fees. |
| `Member` | Manages borrowing, returning, and member borrowing limits. |

---

## 📂 Project Structure

The project is organized into separate files to keep the code clean, readable, and maintainable.

```text
📁 Library_Manager/
│
├── 📄 main.py
│     └── Main application and program execution
│
├── 📄 models.py
│     └── All classes and OOP implementation
│
├── 📄 README.md
│     └── Project documentation
│
├── 📄 output.txt
│     └── Complete console output
│
└── 📄 .gitignore
      └── Files excluded from Git tracking
```

---

## 🚀 Installation & Execution

Follow these steps to run the project on your computer.

### Step 1: Clone the Repository

```bash
git clone https://github.com/HarishSontakke2024/library-manager.git
```

### Step 2: Navigate to the Project Folder

```bash
cd library-manager
```

### Step 3: Check Python Version

```bash
python --version
```

Python 3.12 or later is required.

### Step 4: Run the Application

```bash
python main.py
```

**That's it!** The Library Management System will start running in your terminal.

---

## 🖥️ Sample Program Output

```text
========== LIBRARY MANAGEMENT SYSTEM ==========

--- Borrowing Items ---
Alice borrowed: Book: Python 101 by A. Rao (ID 1)
Could not borrow: Python 101 is already borrowed.
Alice borrowed: Magazine: Tech Today, Issue 45 (ID 2)

--- Borrowing Limit Test ---
Bob borrowed: DVD: Python Tutorial, Duration 120 minutes (ID 3)
Borrowing error: Bob has reached the borrowing limit.

--- Invalid Return Test ---
Return error: Tech Today was not borrowed by Bob.

--- Late Fee Calculation ---
Book: Python 101 by A. Rao (ID 1) -> Late fee for 3 days: Rs 6
Magazine: Tech Today, Issue 45 (ID 2) -> Late fee for 3 days: Rs 3
DVD: Python Tutorial, Duration 120 minutes (ID 3) -> Late fee for 3 days: Rs 15

--- Returning Items ---
Alice returned: Book: Python 101 by A. Rao (ID 1)
Late fee: Rs 6

--- Member Borrowed Lists ---
Alice's borrowed items: ['Tech Today']
Bob's borrowed items: ['Python Tutorial']

--- Item Availability ---
Book available: True
Magazine available: False
DVD available: False

--- Encapsulation Test ---
Cannot access private availability directly!
Correct availability check: True

--- Total Items ---
Total items created: 3

========== PROGRAM FINISHED ==========
```

📌 For the complete console output, refer to [`output.txt`](output.txt).

---

## 📝 Assignment Reflection

### Q1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

`LibraryItem` is abstract because it provides common features to all library items but should not be directly instantiated. Every child class must implement its own `late_fee()` method. If DVD does not implement this abstract method, Python raises a `TypeError` when we try to create a DVD object.

### Q2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

Accessing `item.__available` from outside the class raises an `AttributeError` because Python uses name mangling for double-underscore attributes. We use `is_available()` to check availability safely without directly accessing the private variable.

### Q3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a class attribute shared by all objects of the LibraryItem hierarchy, and it keeps track of the total number of items created. On the other hand, `self.title` is an instance attribute, meaning every individual item has its own title.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding and implementing Object-Oriented Programming.
- Creating abstract classes and abstract methods.
- Using inheritance to reuse code.
- Implementing encapsulation using private attributes.
- Understanding polymorphism through method overriding.
- Handling invalid operations using exceptions.
- Working with class attributes and instance attributes.
- Organizing a Python project into multiple files.
- Using Git and GitHub for version control.

---

## 🔮 Future Improvements

Some features that could be added in future versions:

- 📅 Borrowing and return dates.
- 🔍 Search items by title or ID.
- 📋 Display all available library items.
- 👥 Add and remove library members.
- 💾 Store library records using a database.
- 🖥️ Develop a graphical user interface.

---


<p align="center">
  <b>⭐ Thank you for visiting this project! ⭐</b>
</p>

