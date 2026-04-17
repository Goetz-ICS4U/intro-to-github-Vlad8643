"""
author: Vlad
date: 03.10.2026
1.0 Try / Except
"""

def valid_age_01 ():
    age = 151
    while age >150 or age < 0:
       
        try:
            age = int(input("Input your age: "))
            if age <=150 and age >= 0:
                return age
            else:
                print("Age must be between 0 and 150.")

        except ValueError:
            print("Please input proper age")
            age = 151

def averaging_02():

    #i = 0
    n_to_input= 0
    while n_to_input <=0:
        try:
            total_sum = 0
            n_to_input = int(input("How many numbers you want to input: "))
            if n_to_input <= 0:
                print("Number must be positive")
                continue
            for i in range(n_to_input):
                total = int(input(f"Input your {i+1} value: "))
                total_sum += total
            aver= total_sum / n_to_input
            print(f"The average is {aver:.2f}")
            break
       
        except ValueError:
            print("Please input integer")
            n_to_input = 0
            
    
def nameopen_03 ():
    filename = "retry"
    while filename != "quit":
        try:

            filename = input("\nEnter filename to read (or type 'quit' to exit): ").strip()
            if filename.lower() == "quit":
                print("Exiting file reader. Goodbye!")
                break
            with open(filename, "r") as file:
                print(f"\n--- Contents of {filename} ---")
                print(file.read())
        except FileNotFoundError:
            print("No file found")
        except Exception as e:
            print (f"Error:", e)
            filename = "retry"


def conversion_04():
    choice = 0 
    while choice != 1 and choice != 2:
        try:
            choice = int(input("1 = F to C and 2 = C to F: " ))
            if choice ==1:
                tempF = float(input("Input temperature in F: "))
                tempC = (tempF - 32) * (5/9)
                print(f"The {tempF:.2f}F is {tempC:.2f}C")
                break
            elif choice == 2:
                tempC = float(input("Input temperature in C: "))
                tempF = (tempC*(9/5)) +32
                print(f"The {tempC:.2f}C is {tempF:.2f}F")
                break
            else:
                print("Invalid choice") 
        except ValueError:
            print("Please input integer")
            choice = 0

def display_menu():
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_choice05():
    choice = 0
    while choice < 1 or choice > 5:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
               return choice
            else:
                print("Please enter a number between 1 and 5!")
        except ValueError:
            print("Please enter an integer")
            choice = 0
                
def main():

    """Simple calculator - needs exception handling!"""
    choice = 0
    while choice != 5:
        display_menu()
        choice = get_choice05()
        # Exits the menu immediately
        if choice == 5:
            print("Goodbye!")
            break 

        # skips to next iteration
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers")
            continue
            
        if choice == 1:
            print(f"Result: {num1 + num2:.2f}")
        elif choice == 2:
            print(f"Result: {num1 - num2:.2f}")
        elif choice == 3:
            print(f"Result: {num1 * num2:.2f}")
        elif choice == 4:
            try:
                result = num1 / num2
                print(f"Result: {result:.2f}")
            except ZeroDivisionError:
                print("Can not divide by zero")
       

if __name__ == "__main__":
    age = valid_age_01()
    print(f"Age recorded: {age}")
    averaging_02()
    nameopen_03()
    conversion_04()
    main()