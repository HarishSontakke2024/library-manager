
from models import Book, Magazine, DVD, Member, LibraryItem


# Create library items
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 45)
dvd = DVD("Python Tutorial", 3, 120)


# Create two members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


print("========== LIBRARY MANAGEMENT SYSTEM ==========")


# 1. Borrowing with error handling
print("\n--- Borrowing Items ---")

try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())

    bob.borrow(book)

except ValueError as e:
    print("Could not borrow:", e)


# 2. Test borrowing another item
try:
    alice.borrow(magazine)
    print("Alice borrowed:", magazine.describe())

except ValueError as e:
    print("Could not borrow:", e)


# 3. Test borrowing limit
print("\n--- Borrowing Limit Test ---")

try:
    bob.borrow(dvd)
    print("Bob borrowed:", dvd.describe())

    bob.borrow(magazine)

except ValueError as e:
    print("Borrowing error:", e)


# 4. Test returning an item not borrowed
print("\n--- Invalid Return Test ---")

try:
    bob.return_item(magazine)

except ValueError as e:
    print("Return error:", e)


# 5. Polymorphism: calculate late fees
print("\n--- Late Fee Calculation ---")

items = [book, magazine, dvd]

for item in items:
    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# 6. Return an item
print("\n--- Returning Items ---")

try:
    fee = alice.return_item(book, 3)
    print("Alice returned:", book.describe())
    print("Late fee: Rs", fee)

except ValueError as e:
    print("Return error:", e)


# 7. Show borrowed items
print("\n--- Member Borrowed Lists ---")

print("Alice's borrowed items:", alice.borrowed_titles())
print("Bob's borrowed items:", bob.borrowed_titles())


# 8. Check availability
print("\n--- Item Availability ---")

print("Book available:", book.is_available())
print("Magazine available:", magazine.is_available())
print("DVD available:", dvd.is_available())


# 9. Demonstrate encapsulation
print("\n--- Encapsulation Test ---")

try:
    print(book.__available)

except AttributeError:
    print("Cannot access private availability directly!")

print("Correct availability check:", book.is_available())


# 10. Total items created
print("\n--- Total Items ---")

print("Total items created:", LibraryItem.total_items)

print("\n========== PROGRAM FINISHED ==========")
