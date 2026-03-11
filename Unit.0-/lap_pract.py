# ## Task:
#     Create a simple calculator program in Python that allows users to perform basic arithmetic operations repeatedly until they choose to exit.


#     Greets the user with a welcome message.


#     Prompts the user to enter two numbers and an operator (+, -, *, or /).


#     Performs the chosen operation and displays the result formatted to two decimal places.


#     Handles invalid operators and division by zero gracefully.


#     Repeats the process in a loop until the user decides to quit.


#     If you have time, create functions for your operations so that you can just call the function under main.


# Copy the code below and name it calculator.py to get started.
# ``` Python


import datetime




"""
ADD HEADER COMMENTS
"""
def calculate_operation(num1: float, num2: float, opr: str) -> float:
    """
    TODO: Write the docstring, argument, and return


    Example:
    >>> calculate_operation(3.0, 2.0, *)
    6.0
    """
    # TODO: Implement this function so you can use it in your main()
    # Use if/elif statements to perform the correct operation
    # Handle division by zero and invalid operators
    # If the operator is invalid, print "Invalid operation"
    # and set ans = num1


   
    if opr == "+":
        answer = num1 + num2
    elif opr == "-":
        answer = num1 - num2
    elif opr == "*":
        answer = num1 * num2
    elif opr == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            answer = num1
        else:
            answer = num1 / num2
    elif opr == "%":
        if num2 == 0:
            print("Cannot divide by zero.")
            answer = num1
        else:
            answer = num1 % num2
    else:
        print("Invalid operation")
        answer = num1




    return (f"{num1:.2f} {opr} {num2:.2f} = {answer:.2f}")


def add_calculation_history(history_list: list[str], calculation:str) -> list[str]:
    """
    Returns the list of all past calculations, including invalid inputs.


    Args:
        history_list (list[str]): the list of past calculations in a program
        calculation(str): the current calculation you want to add into history_list
   
    Return:
        list[str]: the list of all the past calculations, including the calculation you just added.
   
    Example:
    >>> add_calculation_history([3.5 + 3.5 = 7.0, 4 % 2 = 0], 3 + 1 = 4)
    [3.5 + 3.5 = 7.0, 4 % 2 = 0, 3 + 1 = 4]
    """


    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} --> {calculation}"


    history_list.append(entry)
    return history_list
   
def main():
    """
    Main program to run the interactive calculator.
    """
    # TODO: write a print statement to greet the user


    # Add IPO Comments
    choice = 0
    history_list = []
 
    while True:
        print("\nChoose an option below:")
        print("1. Make a calculation")
        print("2. See Past Calculations")
        print("3. Exit")


        choice = input("\nEnter Choice: ").strip()


        if choice == "1":
             keep_calculating = True
             while keep_calculating:
               
            # TODO: Prompt the user to input the first number
                print("Welcome to my calculator app. ")
                num1 = float(input("num1> "))
       
                # TODO: Prompt the user to input one of these operator (+, -, *, /, %)
                opr = (input("op> "))


                # TODO: Prompt the user to input the second number
                num2 = float(input("num2> "))


                # TODO: call calculate_operation function to store the result into variable 'ans'
                ans = calculate_operation(num1, num2, opr)


                # TODO: Print the result in the format:
                # "%.2f %c %.2f = %.2f" using f-strings
                print(ans)


                # TODO: Add the calculation into the history list using add_calculation_history function
                history_list = add_calculation_history(history_list, ans)
                # TODO: print out all past calculations
                print(f"Past calculations: {history_list}")
                # Ask the user if they want to continue using the calculator
                cont = input("Do you want to perform another calculation? (yes/no)> ").lower().strip()
               
                if cont != "yes" and cont != "y":
                    keep_calculating = False
                    print("Returning to menu...")
                   


        elif choice == "2":
            print("\nPast Calculations:")
            if not history_list:
                print("No history yet.")
            else:
                for item in history_list:
                    print(item)
        elif choice == "3":
                print("Goodbye!")
                break
        else:
                print("Invalid input! Please choose 1, 2, or 3.")    


## Sample Output:
#     Welcome to my calculator app.
#     num1> 12.5
#     op> +
#     num2> 7.3
#     12.50 + 7.30 = 19.80
#     Past calculations: [12.50 + 7.30 = 19.80]
#     Do you want to perform another calculation? (yes/no)> yes


#     num1> 15
#     op> /
#     num2> 0
#     Cannot divide by zero.
#     15.00 / 0.00 = 15.00
#     Past calculations: [12.50 + 7.30 = 19.80, 15.00 / 0.00 = 15.00]
#     Do you want to perform another calculation? (yes/no)> yes
   
#     num1> 9
#     op> $
#     num2> 3
#     Invalid operation
#     9.00 $ 3.00 = 9.00
#     Past calculations: [12.50 + 7.30 = 19.80, 15.00 / 0.00 = 15.00, 9.00 $ 3.00 = 9.00]
#     Do you want to perform another calculation? (yes/no)> no
#     Goodbye!


# ## Extension
# If you finished building your calculator, add these enhancements to better prepare you for the lab (especially for Gold Tier).


#     1. Save a History of Calculations with Time Stamps:
#     - Your calculator should keep track of all past computations, including the date and time they were done.
#     - If the user asks to see the history, print out each calculation with its timestamp.
#     Hint: Use the datetime module to get the current time.


#     2. Improve User Input for Continuing:
#     - When asking if the user wants to continue, make sure your program accepts different versions of "yes" and "no" (e.g., "Yes", "YES", "no", "No", etc.).
#     - Also, handle cases where the user types something unexpected. ex. user typed "BLAH"


#     3. Create an user-friendly Menu:
#     - Have a menu with options that user can choose when using the calculator. See the sample output below.


# ## Sample Output for User-Friendly
#     Welcome to my calculator app.


#     Choose an option below:
#     1. Make a calculation
#     2. See Past Calculations
#     3. Exit


#     Enter Choice: 1
#     num1> 12.5
#     op> +
#     num2> 7.3
#     12.50 + 7.30 = 19.80


#     Choose an option below:
#     1. Make a calculation
#     2. See Past Calculations
#     3. Exit


#     Enter Choice: 2
#     Past Calculations:
#     2026-02-20 13:54:54.809971 --> 12.50 + 7.30 = 19.80


#     Choose an option below:
#     1. Make a calculation
#     2. See Past Calculations
#     3. Exit


#     Enter Choice: blah
#     Invalid input!


#     Choose an option below:
#     1. Make a calculation
#     2. See Past Calculations
#     3. Exit
   
#     Enter Choice: 3
#     Goodbye!


if __name__ == "__main__":
    main()



