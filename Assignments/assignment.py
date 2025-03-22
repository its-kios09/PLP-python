# ProgFunA1_s1234567.py
# Student Name: John Doe
# Student ID: s1234567
# Highest Part Attempted: Part 3
# Problems/Unmet Requirements: None

import sys

# Initialize data structures
customers = {"Emily": True, "James": False}  # True indicates membership
members = {"Emily"}
book_categories = {
    "Fantasy": {"type": "Rental", "prices": [0.5, 0.4], "books": ["Harry Potter 1", "The Hobbit"]},
    "Crime": {"type": "Rental", "prices": [0.5, 0.4], "books": ["Gone Girl", "Sherlock Holmes 1"]},
    "Classics": {"type": "Rental", "prices": [0.3, 0.25], "books": ["Pride and Prejudice"]},
    "Modern Classics": {"type": "Rental", "prices": [0.4, 0.3], "books": ["To Kill a Mockingbird"]},
    "History": {"type": "Rental", "prices": [0.4, 0.3], "books": ["The Diary of a Young Girl"]},
    "Philosophy": {"type": "Rental", "prices": [0.3, 0.25], "books": ["The Republic"]},
    "Science": {"type": "Rental", "prices": [0.5, 0.4], "books": ["A Brief History of Time"]},
    "Textbooks": {"type": "Reference", "prices": [0.75, 0.6], "books": ["Introduction to the Theory of Computation"]},
    "Art": {"type": "Rental", "prices": [0.5, 0.4], "books": ["The Story of Art"]},
    "Other": {"type": "Reference", "prices": [0.5, 0.4], "books": ["Thinking Fast and Slow", "Atomic Habits"]},
}
rental_history = {}  # Stores rental history for each customer

def display_menu():
    print("\nMenu:")
    print("1. Rent a book")
    print("2. Update information of a book category")
    print("3. Update books of a book category")
    print("4. Display existing customers")
    print("5. Display existing book categories")
    print("6. Display the most valuable customer")
    print("7. Display a customer rental history")
    print("8. Exit")

def get_valid_name():
    while True:
        name = input("Enter the customer's name: ").strip()
        if name.isalpha():
            return name
        print("Error: Name must contain only alphabet characters. Please try again.")

def get_valid_book():
    while True:
        book = input("Enter the name of the book: ").strip()
        for category in book_categories.values():
            if book in category["books"]:
                return book
        print("Error: Book not found. Please try again.")

def get_valid_days(book):
    while True:
        try:
            days = int(input("Enter the number of borrowing days: ").strip())
            if days <= 0:
                print("Error: Number of days must be a positive integer. Please try again.")
                continue
            category = next(cat for cat in book_categories.values() if book in cat["books"])
            if category["type"] == "Reference" and days > 14:
                print("Error: Reference books can only be borrowed for up to 14 days. Please try again.")
                continue
            return days
        except ValueError:
            print("Error: Invalid input. Please enter a positive integer.")

def calculate_cost(book, days, is_member):
    category = next(cat for cat in book_categories.values() if book in cat["books"])
    price = category["prices"][0] if days <= 10 else category["prices"][1]
    original_cost = price * days
    discount = original_cost * 0.1 if is_member and book not in rental_history.get(customer_name, []) else 0
    total_cost = original_cost - discount
    return original_cost, discount, total_cost

def rent_book():
    global customers, rental_history
    customer_name = get_valid_name()
    if customer_name not in customers:
        customers[customer_name] = False  # New customer is not a member by default
    is_member = customers[customer_name]

    rented_books = []
    while True:
        book = get_valid_book()
        days = get_valid_days(book)
        original_cost, discount, total_cost = calculate_cost(book, days, is_member)
        rented_books.append((book, days, original_cost, discount, total_cost))

        if customer_name not in rental_history:
            rental_history[customer_name] = []
        rental_history[customer_name].append((book, days, original_cost, discount, total_cost))

        another = input("Do you want to rent another book? (y/n): ").strip().lower()
        while another not in ["y", "n"]:
            print("Error: Invalid input. Please enter 'y' or 'n'.")
            another = input("Do you want to rent another book? (y/n): ").strip().lower()
        if another == "n":
            break

    # Display receipt
    print("\n------------------------------------------------------------------------------------------")
    print(f"Receipt for {customer_name}")
    print("------------------------------------------------------------------------------------------")
    print("Books rented:")
    for book, days, _, _, _ in rented_books:
        category = next(cat for cat in book_categories.values() if book in cat["books"])
        price = category["prices"][0] if days <= 10 else category["prices"][1]
        print(f" - {book} for {days} days ({price:.2f} AUD/day)")
    print("------------------------------------------------------------------------------------------")
    total_original_cost = sum(item[2] for item in rented_books)
    total_discount = sum(item[3] for item in rented_books)
    total_final_cost = sum(item[4] for item in rented_books)
    print(f"Original cost: {total_original_cost:.2f} AUD")
    print(f"Discount: {total_discount:.2f} AUD")
    print(f"Total cost: {total_final_cost:.2f} AUD")
    print("------------------------------------------------------------------------------------------")

    # Ask if the customer wants to become a member
    if not is_member:
        response = input("Would you like to become a member? (y/n): ").strip().lower()
        while response not in ["y", "n"]:
            print("Error: Invalid input. Please enter 'y' or 'n'.")
            response = input("Would you like to become a member? (y/n): ").strip().lower()
        if response == "y":
            customers[customer_name] = True
            members.add(customer_name)
            print("Congratulations! You are now a member.")

def update_book_category():
    while True:
        try:
            input_str = input("Enter book category, type, price_1, price_2 (comma-separated): ").strip()
            parts = [part.strip() for part in input_str.split(",")]
            if len(parts) != 4:
                print("Error: Invalid format. Please try again.")
                continue
            category, type_, price_1, price_2 = parts
            if category not in book_categories:
                print("Error: Book category not found. Please try again.")
                continue
            if type_ not in ["Rental", "Reference"]:
                print("Error: Type must be 'Rental' or 'Reference'. Please try again.")
                continue
            price_1 = float(price_1)
            price_2 = float(price_2)
            if price_1 <= 0 or price_2 <= 0:
                print("Error: Prices must be positive. Please try again.")
                continue
            book_categories[category]["type"] = type_
            book_categories[category]["prices"] = [price_1, price_2]
            print("Book category updated successfully.")
            break
        except ValueError:
            print("Error: Invalid input. Please try again.")

def update_books():
    while True:
        action = input("Do you want to add (a) or remove (r) books? ").strip().lower()
        if action not in ["a", "r"]:
            print("Error: Invalid input. Please enter 'a' or 'r'.")
            continue
        input_str = input("Enter book category and books (comma-separated): ").strip()
        parts = [part.strip() for part in input_str.split(",")]
        if len(parts) < 2:
            print("Error: Invalid format. Please try again.")
            continue
        category, books = parts[0], parts[1:]
        if category not in book_categories:
            print("Error: Book category not found. Please try again.")
            continue
        if action == "a":
            existing_books = set(book_categories[category]["books"])
            new_books = [book for book in books if book not in existing_books]
            if new_books:
                book_categories[category]["books"].extend(new_books)
                print(f"Added books: {', '.join(new_books)}")
            else:
                print("No new books to add.")
        else:
            existing_books = set(book_categories[category]["books"])
            removed_books = [book for book in books if book in existing_books]
            if removed_books:
                book_categories[category]["books"] = [book for book in book_categories[category]["books"] if book not in removed_books]
                print(f"Removed books: {', '.join(removed_books)}")
            else:
                print("No existing books to remove.")
        break

def display_customers():
    print("\nExisting Customers:")
    for customer, is_member in customers.items():
        status = "Member" if is_member else "Non-Member"
        print(f"{customer}: {status}")

def display_book_categories():
    print("\nExisting Book Categories:")
    for category, details in book_categories.items():
        print(f"{category}:")
        print(f"  Type: {details['type']}")
        print(f"  Prices: {details['prices'][0]:.2f} AUD/day (<= 10 days), {details['prices'][1]:.2f} AUD/day (> 10 days)")
        print(f"  Books: {', '.join(details['books'])}")

def display_most_valuable_customer():
    if not rental_history:
        print("No rental history available.")
        return
    total_spent = {}
    for customer, rentals in rental_history.items():
        total_spent[customer] = sum(rental[4] for rental in rentals)
    max_spent = max(total_spent.values())
    valuable_customers = [customer for customer, spent in total_spent.items() if spent == max_spent]
    print("\nMost Valuable Customer(s):")
    for customer in valuable_customers:
        print(f"{customer}: {max_spent:.2f} AUD")

def display_customer_rental_history():
    while True:
        customer_name = input("Enter the customer's name: ").strip()
        if customer_name in rental_history:
            print(f"\nRental History for {customer_name}:")
            for i, rental in enumerate(rental_history[customer_name], 1):
                book, days, original_cost, discount, total_cost = rental
                print(f"Rental {i}:")
                print(f"  Book: {book}, Days: {days}")
                print(f"  Original Cost: {original_cost:.2f} AUD")
                print(f"  Discount: {discount:.2f} AUD")
                print(f"  Total Cost: {total_cost:.2f} AUD")
            break
        print("Error: Customer not found. Please try again.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            rent_book()
        elif choice == "2":
            update_book_category()
        elif choice == "3":
            update_books()
        elif choice == "4":
            display_customers()
        elif choice == "5":
            display_book_categories()
        elif choice == "6":
            display_most_valuable_customer()
        elif choice == "7":
            display_customer_rental_history()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()