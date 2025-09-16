import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (Food, Travel, etc.): ").capitalize()
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date_time])

        print("Expense added successfully!\n")

    except ValueError:
        print(" Invalid amount! Please enter a number.\n")


# Function to view all expenses
def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\nYour Expenses:")
            print("-" * 40)
            for row in reader:
                amount, category, date_time = row
                print(f" {amount} |  {category} |  {date_time}")
            print("-" * 40 + "\n")
    except FileNotFoundError:
        print("️ No expenses found! Add some first.\n")


# Function to show expense summary
def summary():
    try:
        total = 0
        categories = {}

        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                amount, category, date_time = row
                amount = float(amount)
                total += amount
                categories[category] = categories.get(category, 0) + amount

        print("\n Expense Summary")
        print("-" * 40)
        print(f"Total Spent:  {total}")
        for cat, amt in categories.items():
            print(f"{cat}: {amt}")
        print("-" * 40 + "\n")

    except FileNotFoundError:
        print("No expenses found! Add some first.\n")


# Main menu
def main():
    while True:
        print("===== Expense Book =====")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Show Summary")
        print("4️⃣ Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            print(" Exiting... Have a nice day!")
            break
        else:
            print(" Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
