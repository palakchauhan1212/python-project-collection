Expense Tracker is a command-line based Expense Tracker developed in Python to record, store, analyze, and visualize personal expenses.
This project uses CSV for persistent data storage and makes use of NumPy, Pandas, and Matplotlib for data analysis and graphical representation.

Features

- Add new expenses
- Automatically record the current date
- Store expense data in a CSV file
- View all recorded expenses
- Generate expense reports
- Calculate total expenses
- Identify the highest individual expense
- Analyze category-wise spending
- Analyze monthly spending
- Calculate average spending
- Calculate median spending
- Calculate standard deviation of expenses
- Generate graphical representation of category-wise spending
- Handle invalid user input and runtime errors

Technologies Used

- Python
- CSV
- NumPy
- Pandas
- Matplotlib

Concepts Used

- Object-Oriented Programming
- Classes and Objects
- Constructors
- Functions and Methods
- Conditional Statements
- Loops
- Exception Handling
- File Handling
- CSV File Handling
- Dictionary Data Structures
- List Comprehension
- Lambda Functions
- Date and Time Handling
- Data Analysis with NumPy and Pandas
- Data Visualization with Matplotlib

Data Storage

Expense records are stored in a CSV file named "expenses.csv".

Each record contains the following fields:

Date
Category
Amount
Description

Example:

Date,Category,Amount,Description
03-09-2026,Food,250.0,Lunch
03-09-2026,Travel,100.0,Bus fare
04-09-2026,Education,500.0,Study material

The CSV file is automatically created with the required headers if it does not already exist.

Application Menu

When the program is executed, the following menu is displayed:

1. Add Expense
2. View Expenses
3. Reports
4. NumPy Analysis
5. Graphical Representation
6. Exit

1. Add Expense

Allows the user to enter:

- Expense category
- Expense amount
- Expense description

The current date is automatically assigned to the expense.

Negative expense amounts are rejected.

2. View Expenses

Displays all stored expenses along with:

- Date
- Category
- Amount
- Description

3. Reports

Generates a basic expense report containing:

- Total expenses
- Highest individual expense
- Category-wise spending
- Monthly spending

4. NumPy Analysis

Uses NumPy to calculate basic statistical information:

- Average spending
- Median spending
- Standard deviation

5. Graphical Representation

Uses Pandas to read the stored CSV data and group expenses according to category.

Matplotlib is then used to display the category-wise spending graph.

Installation

Make sure Python is installed on your system.

Install the required libraries:

pip install -r requirements.txt

Requirements

Requires following external libraries:

numpy
pandas
matplotlib

The "csv", "os", and "datetime" modules are part of Python's standard library and do not need to be installed separately.

Running the Project

Run the Python file using:

python expense_tracker_&_budget_analyzer.py

«Replace "employee_attendance_system.py" with your actual Python filename if it has a different name.»

The application will start in the terminal and display the main menu.

Data Analysis

The project uses different Python libraries for different purposes.

NumPy

NumPy is used for numerical and statistical calculations such as:

Mean
Median
Standard Deviation

Pandas

Pandas is used to read and process the CSV data and perform category-wise grouping.

Matplotlib

Matplotlib is used to create a graphical representation of category-wise expenses.

Error Handling

The program uses exception handling to prevent unexpected input or runtime errors from terminating the application immediately.

Examples of handled situations include:

- Invalid menu input
- Invalid numeric input
- Negative expense amounts
- File-related errors

Objectives

This project was developed to practice and demonstrate:

- Python Object-Oriented Programming
- File handling
- CSV data storage
- Exception handling
- Data structures
- NumPy-based statistical analysis
- Pandas-based data processing
- Matplotlib-based visualization
- Building a menu-driven Python application

Author

Developed by Palak as part of a Python learning journey.