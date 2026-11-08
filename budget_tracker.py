import json
import os
from datetime import datetime
if os.path.exists("budget_data.json"):
    with open("budget_data.json", "r") as file:
        data = json.load(file)
        incomes = data["incomes"]
        expenses = data["expenses"]
        budget = data.get("budget", 0)
else:
    incomes=[]
    expenses=[]
    budget=0
def save_data():
    data = {
        "incomes": incomes,
        "expenses": expenses,
        "budget":budget
    }
    with open("budget_data.json", "w") as file:
        json.dump(data, file, indent=4)
while True:
    print("===== BUDGET TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Financial Summary")
    print("4. Set Budget")
    print("5. Exit")
    print("6. view all transactions")
    choice=input("enter your choice")
    if choice=="1":
        source=input("enter income source")
        try:
            amount=float(input("enter income amount"))
        except ValueError:
            print("please enter a valid number")
            continue
        if amount <=0:
            print("amount must be greater than 0")
        income_record={
            "source":source,
            "amount":amount,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        incomes.append(income_record)
        save_data()
        print("income added succesfully")
        print("income source",source)
        print("income amount",amount)
    elif choice=="2":
        category=input("enter expense category")
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if amount<=0:
            print("amount should be greater than 0")
            continue
        expense_record={
            "category":category,
            "amount":amount,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        expenses.append(expense_record)
        save_data()
        print("expense added succesfully")
        print("expense category",category)
        print("expense amount",amount)
    elif choice=="3":
        total_income=0
        total_expenses=0
        for record in incomes:
            total_income=total_income+record["amount"]
        for record in expenses:
            total_expenses=total_expenses+record["amount"]
        balance=total_income-total_expenses
        print("Total Income",total_income)
        print("Total Expenses",total_expenses)
        print("Remaining Balance",balance)
        if budget > 0 and total_expenses > budget:
            print("WARNING: You have exceeded your budget")
    elif choice == "4":
        try:
            budget = float(input("Enter your budget limit: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if budget <= 0:
            print("Budget must be greater than zero")
            continue
        print("Budget set successfully")
        print("Your budget limit is:", budget)
        save_data()
    elif choice=="5":
        print("Thank You")
        break
    elif choice=="6":
        if len(incomes)==0 and len(expenses)==0:
            print("No transactions found")
        else:
            print("\n--- INCOME TRANSACTIONS ---")
            if len(incomes)==0:
                print("No income records found")
            else:
                print("income records")
                for income in incomes:
                    print(income["source"], income["amount"],
                    income.get("date_time", "Date not available"))
            print("\n--- EXPENSE TRANSACTIONS ---")
            if len(expenses)==0:
                print("No expense records found")
            else:
                print("expense records")
                for expense in expenses:
                    print(expense["category"], expense["amount"],
                    expense.get("date_time", "Date not available"))
    else:
        print("Invalid choice or try again")
