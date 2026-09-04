Quiz Management System is a command-line based Quiz Management System developed in Python. The application provides separate interfaces for administrators and students, allowing administrators to manage quiz questions and students to take quizzes and track their scores.
The system also maintains participant attempt records and provides statistical analysis of quiz performance using NumPy.

Features

Admin Module

- Add new quiz questions
- Add corresponding answers
- Prevent duplicate questions and answers
- Delete existing questions
- View all available questions and answers
- Automatically save questions to a JSON file
- Record successful administrative activities in a log file

Student Module

- Take the available quiz
- Enter participant name
- Automatically calculate the quiz score
- Store scores for multiple attempts
- Track the number of attempts made by each participant
- View individual participant scores
- Store attempt information in a JSON file

Analysis Module

The analysis module uses NumPy to calculate:

- Highest score
- Lowest score
- Average score

Logging System

The project includes a custom decorator-based activity logging system.

Successful actions such as:

- Adding a question
- Deleting a question
- Taking a quiz

are recorded with a timestamp in the log file.

Technologies Used

- Python
- JSON
- NumPy
- OS module
- datetime module
- functools

Concepts Used

- Object-Oriented Programming
- Classes and Objects
- Inheritance
- Methods
- Constructors
- Decorators
- "functools.wraps"
- Higher-order functions
- File Handling
- JSON Serialization and Deserialization
- Exception Handling
- Dictionaries
- Lists
- Loops
- Conditional Statements
- Lambda Functions
- String Manipulation
- Date and Time Handling
- NumPy-based Data Analysis

Application Architecture

The application is divided into three major components:

                         Quiz Management System
                                  |
                +-----------------+-----------------+
                |                 |                 |
              Admin            Student          Analysis
                |                 |                 |
          CreateQuiz         AttemptQuiz          Quiz
                |                 |                 |
        +-------+-------+    +----+-----+      NumPy
        |       |       |    |          |      Analysis
       Add    Delete   View  Take     View
       Quiz   Quiz     Quiz  Quiz     Score

Class Structure

Quiz

"Quiz" is the base class of the application.

It is responsible for:

- Initializing file paths
- Creating required files
- Loading quiz data
- Saving quiz data
- Loading participant attempts
- Saving participant attempts
- Performing score analysis

CreateQuiz

"CreateQuiz" inherits from the "Quiz" class.

It provides administrator functionality such as:

add_que()
delete_que()
view_que()
quiz_main()

AttemptQuiz

"AttemptQuiz" also inherits from the "Quiz" class.

It provides student functionality such as:

take_quiz()
view_score()
attempt_main()

log_activities Decorator

The "log_activities()" decorator is used to record successful activities performed by the application.

It:

1. Receives an action name.
2. Wraps the target function.
3. Executes the function.
4. Checks whether the operation was successful.
5. Records the timestamp and arguments.
6. Writes the activity to "logs.txt".

The decorator uses "functools.wraps" to preserve the metadata of the decorated function.

Data Storage

The application uses JSON files for persistent storage.

quiz.json

This file stores quiz questions and answers.

Example structure:

{
    "1": {
        "Que": "What is Python?",
        "Ans": "Programming Language"
    },
    "2": {
        "Que": "What does CPU stand for?",
        "Ans": "Central Processing Unit"
    }
}

attempt.json

This file stores participant information, number of attempts, and scores.

Example structure:

{
    "Student": {
        "Attempts": 2,
        "Score": [2, 3]
    }
}

logs.txt

The log file stores successful activities performed by the application along with timestamps.

Application Menu

When the program starts, the user is presented with the following options:

=============== HOME ===============

Enter (Admin/Student/Analysis/Exit):

The available modes are:

Admin
Student
Analysis
Exit

Admin Workflow

After selecting "Admin", the following menu is displayed:

1. Add Question
2. Delete Question
3. View Question
4. Exit to Home

Add Question

The administrator can enter a question and its answer.

The system checks for:

- Blank questions
- Duplicate questions
- Duplicate answers

Valid questions are stored in "quiz.json".

Delete Question

The administrator can enter an existing question to remove it from the quiz.

After deletion, the remaining question numbers are rearranged.

View Question

Displays all questions and their corresponding answers stored in the quiz.

Student Workflow

After selecting "Student", the following menu is displayed:

1. Take Quiz
2. View Score
3. Exit to Home

Take Quiz

The student provides their name and answers each question.

The application compares the entered answer with the stored answer and increases the score for every correct response.

The result is then stored in "attempt.json".

If the same participant takes the quiz multiple times, the application:

- Increases the attempt count
- Stores the new score
- Preserves previous scores

View Score

Allows the participant to enter their name and view:

- Participant name
- Number of attempts
- Scores from previous attempts

Statistical Analysis

The Analysis option uses NumPy to process all recorded scores.

The application calculates:

Highest Score
Lowest Score
Average Score

The scores are extracted from the participant attempt records and converted into a NumPy array before performing the calculations.

Logging

The project uses a custom decorator:

@log_activities("Add Question")

and:

@log_activities("Delete Question")

and:

@log_activities("Takes Quiz")

This demonstrates how decorators can be used to add additional functionality to existing methods without modifying their core logic.

Error Handling

The application uses exception handling in multiple areas to handle unexpected situations.

Examples include:

- File-related errors
- Invalid menu input
- Invalid numeric input
- JSON loading errors
- JSON saving errors
- Log file errors

The program attempts to continue running instead of terminating immediately when an exception occurs.

Installation

Make sure Python is installed on your system.

Install the required external library:

pip install -r requirements.txt

Requirements

The project currently requires:

numpy

The following modules are part of Python's standard library and do not require separate installation:

os
json
datetime
functools

Running the Project

Run the Python program using:

python quiz.py

«Replace "employee_attendance_system.py" with your actual Python filename if it has a different name.»

The application will start in the terminal and display the home menu.

Objectives

This project was developed to practice and demonstrate:

- Object-Oriented Programming
- Inheritance
- Decorators
- File handling
- JSON data storage
- Exception handling
- Persistent data management
- NumPy-based analysis
- Modular program design
- Command-line application development

Author

Developed by Palak as part of a Python learning journey.