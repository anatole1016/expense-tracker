from storage import load_expenses, save_expenses
from models import Expense
from analysis import category_expenses

def main():
    print("Welcome to Anatolii's Expense Tracker!")

expenses = load_expenses()

def add_expenses():
    try:
        amount  = float(input("Enter expense amount please: "))
        category = input("Enter expense category please: ")
        description = input("Enter expense description please: ")
        date = input("Enter expense date (YYYY-MM-DD): ")
    
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount. Try again.\n")
        

def list_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['date']} | {e['category']} | ${e['amount']} | {e['description']}")
    print()

def main_menu():
    while True:
        print("Expense Tracker Main Menu")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Show Category Chart")
        print("4. Quit")
        choice = input("Select an option: ")
        
        if choice == "1":
            add_expenses()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            category_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
    
if __name__ == "__main__":
    main()
    main_menu()