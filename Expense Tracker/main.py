
expense_list = []


class Expense:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


def add_expense():
    expense_item = input("Enter the name of item: ").strip()

    if not expense_item:
        print("Item name cannot be empty")
        return

    try:
        expense_price = float(input("Enter the price of item: "))

        if expense_price <= 0:
            print("Enter amount greater than 0")
        else:
            new_exp = Expense(expense_item, expense_price)
            expense_list.append(new_exp)
            print("Expense added successfully")

    except ValueError:
        print("Enter a valid number")


def view_expense():
    if not expense_list:
        print("List is Empty")
    else:
        for index, item in enumerate(expense_list, start=1):
            print(f"{index}. {item.name} | {item.price:.2f}")


def total_expenses():
    total_amount = 0

    for item in expense_list:
        total_amount += item.price

    print(f"Your total expenses are: {total_amount:.2f}")


def delete_expense():
    if not expense_list:
        print("List is Empty")
        return

    view_expense()

    try:
        inp = int(input("Enter the expense number which you want to delete: "))

        if inp < 1 or inp > len(expense_list):
            print("Invalid expense number")
        else:
            remove_item = expense_list.pop(inp - 1)
            print(
                f"Removed item: {remove_item.name} | "
                f"Amount: {remove_item.price:.2f}"
            )

    except ValueError:
        print("Enter a valid number")


while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("Program End")
        break

    else:
        print("Invalid choice")
