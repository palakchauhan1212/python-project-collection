import csv
import os
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
        self.store_file = os.path.join(base_dir,"expenses.csv")
        self.create_file_if_not_exists()
        self.expenses_info = []
        self.expenses = self.load_expenses()
    
    def create_file_if_not_exists(self):
        if not os.path.exists(self.store_file):
            try:
                with open(self.store_file,"w",newline='',encoding='utf-8')as file:
                    writer = csv.writer(file)
                    writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            except IOError as e:
                print(f"Error {file}: {e}")

    def load_expenses(self):
        if not os.path.exists(self.store_file):
            with open(self.store_file,'w',newline="",encoding='utf-8')as file:
                writer = csv.writer(file)
                writer.writerow(["Date","Category","Amount","Description"])
            return
        with open(self.store_file,'r')as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Amount'] = float(row['Amount'])
                self.expenses_info.append(row)

    def save_expenses(self,information):
        with open(self.store_file,'a',newline="",encoding='utf=8')as file:
            writer = csv.writer(file)
            writer.writerow([
                information['Date'],
                information['Category'],
                information['Amount'],
                information['Description']
            ])

    def add_expenses(self,date,category,amount,description):
        expenses = {
            'Date':date,
            "Category":category.strip(),
            "Amount":amount,
            "Description":description.strip()
        }
        self.expenses_info.append(expenses)
        self.save_expenses(expenses)
        print("\nExpenses added successfully.\n")

    def view_expenses(self):
        print("\n========== EXPENSES ==========\n")
        if not self.store_file:
            print("No expenses found.\n")
            return
        for i in self.expenses_info:
            print(f"Date -> {i['Date']}\n"
                  f"Category -> {i['Category']}\n"
                  f"Amount -> {i['Amount']}\n"
                  f"Description -> {i['Description']}\n")

    def report(self):
        if not self.store_file:
            print("No expenses found.\n")
            return
        print("\n=========== REPORT ==========\n")
        amount = np.array([amount['Amount'] for amount in self.expenses_info])
        print(f"Total Expenses: {sum(amount):.2f}Rs")
        highest = max(self.expenses_info, key=lambda x:x['Amount'])
        print(f"Highest Expense is {highest['Amount']:.2f}RS in the category {highest['Category']}")
        
        print("\nCATEGORY WISE SPENDING:\n")
        categorywise_spending = {}
        for i in self.expenses_info:
            category = i['Category']
            categorywise_spending[category] = categorywise_spending.get(category,0) + i['Amount']
        for category,total in categorywise_spending.items():
            print(f"{category} -> {total:.2f}Rs")

        print("\nMONTHLY SPENDING:\n")
        monthly_spending = {}
        for i in self.expenses_info:
            month = datetime.strptime(i["Date"],"%d-%m-%Y").strftime("%B %Y")
            monthly_spending[month] = monthly_spending.get(month,0) + i["Amount"]
        for month,total in monthly_spending.items():
            print(f"{month} -> {total:.2f}Rs")

    def statistics(self):
        if not self.store_file:
            print("No expenses found.\n")
            return
        amount = np.array([amount["Amount"] for amount in self.expenses_info])
        print("\n========== ANALYSIS ==========\n")
        print(f"Average Spending: {np.mean(amount):.2f}")
        print(f"Median Spending: {np.median(amount):.2f}")
        print(f"Standard Spending: {np.std(amount):.2f}")

    def graphical(self):
        data = pd.read_csv("expenses.csv")
        category = data.groupby('Category')['Amount'].sum()
        plt.title("\nCategory vs Amount")
        plt.plot(category)
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.scatter(category.index, category.values)
        plt.show()

def main():
    tracker = ExpenseTracker()
    while True:
        print(f"\n1. Add Expense\n"
              f"2. View Expenses\n"
              f"3. Reports\n"
              f"4. NumPy Analysis\n"
              f"5. Graphical Representation\n"
              f"6. Exit")
        try:
            choice = int(input("\nEnter choice:"))
            if choice == 1:
                date = datetime.now().strftime("%d-%m-%Y")
                category = input('Enter category:')
                amount = float(input("Enter amount:"))
                if amount<0:
                    print("Amount cannot be negative.\n")
                    continue
                description = input("Enter description:")
                tracker.add_expenses(date,category,amount,description)

            elif choice == 2:
                tracker.view_expenses()

            elif choice == 3:
                tracker.report()

            elif choice == 4:
                tracker.statistics()

            elif choice == 5:
                tracker.graphical()

            elif choice == 6:
                print("Thank you!")
                break

            else:
                print("Invalid choice")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()