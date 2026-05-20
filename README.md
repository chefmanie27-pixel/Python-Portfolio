
# Python Mini Toolkit: My First Coding Project

## Project Description
The **Python Mini Toolkit** is a beginner-friendly, interactive, menu-based terminal application designed to solve everyday problems and provide useful mini-tools. Built as part of my learning journey at Life Choices, this program showcases fundamental programming logic, clean user input validation, and code modularity by separating core logic into custom modules

---

## Features
The toolkit consists of a central main menu that routes users to three distinct applications:

1. **Grade Calculator:** Prompts the user for a score between 0 and 100, validates the input, and dynamically outputs the corresponding letter grade (A, B, C, D, or F) based on standard grading scales.
2. **Budget Tracker:** Helps users track their monthly finances. It captures total income, dynamically appends itemized expenses to a list, calculates the remaining balance, and provides a warning if the user goes over budget.
3. **Number Guessing Game:** A classic mini-game where the user has exactly 5 attempts to guess a randomly generated secret number between 1 and 50, with helpful "Too high!" or "Too low!" hints along the way.

---

## Python Concepts Used
This project successfully demonstrates and integrates the following core Python concepts covered in class:

* **Variables & Data Types:** Utilized strings, integers, floats, and booleans for data tracking.
* **User Input & Type Casting:** Captured clean text input and cast data types securely using `int()` and `float()`.
* **Control Flow & Conditionals:** Handled logical routing and ranges using `if`, `elif`, and `else` statements.
* **Loops & Loop Control:** Used `while` loops for continuous menu displays and tracking attempts, utilizing `break` and `continue` statements to manage execution flow.
* **Data Structures (Lists):** Used a Python `list` to store and iterate through itemized expense entries dynamically.
* **Functions & Modularization:** Organised code into reusable functions across separate files.
* **Modules:** Imported Python's built-in `random` module alongside a custom `helpers` module to separate the menu driver from application logic.
* **Error Handling:** Implemented `try/except` blocks to catch `ValueError` exceptions and prevent the application from crashing on invalid user input.

## Challenges Faced & Key Learnings
Challenges
File Separation and Scope: One of the main challenges was understanding how to import functions from a custom module (helpers.py) into the main runner (main.py) without breaking global scopes—specifically ensuring the random module was available exactly where it was needed.

Fulfilling Data Structure Requirements: Initially, expenses were just tracked as a running total. Modifying the program to store data dynamically required implementing a list of dictionaries to properly hold both the expense name and amount.

What I Learned & Future Improvements
I learned how to build robust input verification loops to gracefully handle typos and invalid entries without crashing the terminal.

Future Improvements: In the future, I would like to add a data persistence feature (such as saving budget logs to a .txt or .json file) so that user data is saved even after exiting the program.

## How to Run
* Download the helpers.py and main.py files.
* Open it up with the latest version of Visual Studio Code.
* Make sure you have the code runner extension installed.
* To run the code in terminal press: Ctrl + Alt + N or Tap the run button on the top right of the window.
* Select an option and enjoy!

Author

Azhar Manie - Trainee Developer at Life Choices


---

```text
python-mini-toolkit/
  ├── main.py          # The entry point containing the main menu loop
  ├── helpers.py       # Custom module housing the functional mini-tools
  ├── README.md        # Project documentation and reflection
  └── screenshots/     # Terminal execution screenshots demonstrating functionality

