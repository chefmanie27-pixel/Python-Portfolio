import random

# ==========================================
# 1. Grade Calculator
# ==========================================
def grade_calculator():
    while True:
        try:
            score = int(input("Please enter your grade score (0-100): "))
            
            if score < 0 or score > 100:
                print("[!] Invalid score. Please enter a number between 0 and 100.")
                continue 
                
            break 
            
        except ValueError:
            print("[!] Oops! That wasn't a valid number. Please try again.")

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"The grade for the score {score} is: {grade}")


# ==========================================
# 2. Budget Tracker (Updated with Lists)
# ==========================================
def budget_tracker():
    print("Welcome to the Budget Tracker!")
    
    while True:
        try:
            income = float(input("Enter your total monthly income: R"))
            if income < 0:
                print("[!] Income cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("[!] Please enter a valid number for income.")

    # Defining my expense list
    expense_list = []
    total_expenses = 0.0

    while True:
        action = input("\nWould you like to add an expense? (yes/no): ").strip().lower()
        
        if action in ['no', 'n']:
            break
        elif action in ['yes', 'y']:
            try:
                expense_name = input("What is this expense for? (e.g., Rent, Groceries): ").strip()
                expense_amount = float(input(f"Enter amount for '{expense_name}': R"))
                
                if expense_amount < 0:
                    print("[!] Expense amount cannot be negative.")
                    continue
                
                # Appending data to my list
                expense_list.append({"name": expense_name, "amount": expense_amount})
                total_expenses += expense_amount
                print(f"Added R{expense_amount:.2f} for {expense_name}.")
                
            except ValueError:
                print("[!] Invalid amount. Expense not added. Please enter a valid number.")
        else:
            print("[!] Invalid choice. Please type 'yes' or 'no'.")

    remaining_balance = income - total_expenses
    
    print("\n--- Budget Summary ---")
    print(f"Total Income:   R{income:.2f}")
    
    # Iterating through the list to show an itemized receipt layout
    print("\nItemized Expenses:")
    if not expense_list:
        print("  No expenses recorded.")
    else:
        for item in expense_list:
            print(f"  - {item['name']}: R{item['amount']:.2f}")
            
    print("-" * 25)
    print(f"Total Expenses: R{total_expenses:.2f}")
    print(f"Remaining:      R{remaining_balance:.2f}")
    
    if remaining_balance < 0:
        print("Warning: You are over budget! Consider cutting back on non-essentials.")
    elif remaining_balance == 0:
        print("You broke perfectly even this month!")
    else:
        print("Great job! You stayed under budget.")


# ==========================================
# 3. Number Guessing Game
# ==========================================
def guessing_game():
    print("Welcome to my number guesser!")
    print("You have exactly 5 attempts")
    print("So please guess which number I'm thinking of from 1-50!")
    print("-" * 40)

    random_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            remaining_attempts = max_attempts - attempts
            print(f"Attempts remaining: {remaining_attempts}")

            guess = int(input("Enter your guess: "))
            attempts += 1 

            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                print("Congratulations, you have found the correct number. \nYOU WON!!!")
                return

        except ValueError:
            print("Invalid! Please enter a valid number.")

    print("You have reached the max attempts. Better luck next time")
    print(f"The secret number was {random_number}")
