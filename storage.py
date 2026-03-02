import json
import os

EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Error when loading expenses files")
    return []

def save_expenses(expenses):
    try:
        with open(EXPENSES_FILE, 'w') as file:
            json.dump(expenses, file, indent=4)
    except IOError:
        print("Error when saving expenses file")