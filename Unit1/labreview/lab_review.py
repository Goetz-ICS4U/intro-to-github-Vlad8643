"""
author: Vlad
date: 03.24.2026
unit 1 lab review
"""

# ===================== TASK 1 FUNCTIONS =====================


def get_valid_grade():  # TODO: Add type annotation for return type
    """
    # TODO: Write a complete docstring
    # Should explain: what the function does, parameters, return value,
    # and that it uses try/except to handle invalid input
    """
    # TODO: Implement this function using try/except
    grade = 101
    while grade >100 or grade <0:
        try:
            grade = float(input("Enter a grade (0-100): "))
            if grade <=100 and grade>= 0:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please input proper grade")
            grade = 101
       
   
    # HINTS:
    # - Use a while loop to keep asking until valid input
    # - Use try/except to catch ValueError
    # - Check if grade is between 0 and 100
    # - Return the valid grade as a float
   
# ===================== TASK 2 FUNCTION =====================




def is_eligible_for_honour_roll(grd: float, attendance: float, incidents: int) -> bool:
    """
    Returns True if a student is eligible for honour roll using De Morgan's Law, False otherwise.
   
    A student is eligible if ALL of the following are true:
    - Grade >= 80
    - Attendance >= 90
    - Incidents == 0
   
    This function applies De Morgan's Law by checking the negation:
    NOT (grade >= 80 AND attendance >= 90 AND incidents == 0)
   
    Args:
        grade (float): Student's grade (0-100)
        attendance (float): Student's attendance percentage (0-100)
        incidents (int): Number of behavioral incidents
   
    Returns:
        bool: True if eligible for honour roll, False otherwise
    """
    # TODO (Silver): Implement using De Morgan's Law
    # Check for INeligibility first using OR, then return False
    # Otherwise return True


    if grd <80 or attendance <90 or incidents>0:
        return False
    else:
        return True












# ===================== TASK 3 FUNCTIONS =====================




def process_grade_file(input_filename: str, output_filename: str) -> None:




    """
    Reads student grades from a file, calculates class average, and writes a report.
   
    Uses try/except to handle:
    - FileNotFoundError: Creates default file if input doesn't exist (use "except FileNotFoundError as e:")
    - ValueError: Handles invalid grade data in the file (use "except ValueError as e:")
    - IOError: Handles errors when writing output file (use "except IOError as e:")
   
    Args:
        input_filename (str): Name of the input file with student data
        output_filename (str): Name of the output file for the report
    """
   
    valid_grades = []
   
    # 1. Try to open and read the input file
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Warning: '{input_filename}' not found. Creating a default file.")
        create_default_grade_file(input_filename)
        # Try reading it again after creating it
        with open(input_filename, 'r') as file:
            lines = file.readlines()




    # 2. Process data and handle ValueErrors
    for line in lines:
        if not line.strip(): continue  # Skip empty lines
       
        try:
            _, grade_str = line.strip().split(',')
            grade = float(grade_str.strip())
            valid_grades.append(grade)
        except ValueError:
            print(f"Skipping invalid data: {line.strip()}")




    # 3. Calculate class average
    if valid_grades:
        average = sum(valid_grades) / len(valid_grades)
        report_content = f"Class Average: {average:.2f}\nTotal Students: {len(valid_grades)}"
    else:
        report_content = "No valid grades found to calculate an average."




    # 4. Write report and handle IOErrors
    try:
        with open(output_filename, 'w') as out_file:
            out_file.write("--- Grade Report ---\n")
            out_file.write(report_content)
        print(f"Report successfully written to '{output_filename}'.")
    except IOError as e:
        print(f"Error writing to file: {e}")








    # TODO (Gold): Implement this function
    # 1. Try to open and read the input file
    #    - Use try/except for FileNotFoundError (except FileNotFoundError as e:)
    #    - If file doesn't exist, create a default one
    # 2. Go through each line (format: "Name,Grade")
    #    - Use try/except for ValueError when converting grade (except ValueError as e:)
    #    - Keep track of valid grades for average calculation
    # 3. Calculate class average
    # 4. Write report to output file
    #    - Use try/except for IOError (except IOError as e:)
   
   








def create_default_grade_file(filename: str) -> None:
    """
    Creates a default grade file with sample student data.
   
    Args:
        filename (str): Name of the file to create
    """

    sample_data = [
        "Alice,85",
        "Bob,92",
        "Charlie,78",
        "David,invalid",
        "Eve,95"
    ]
   
    with open(filename, 'w') as file:
        for line in sample_data:
            file.write(line + "\n")




    # TODO (Gold): Implement this helper function
    # Create a file with sample data like:
    # Alice,85
    # Bob,92
    # Charlie,78
    # David,invalid
    # Eve,95
   
# ===================== MAIN =====================




def main() -> None:
    """
    Main function that runs the grade analyzer.
    """
    print("Welcome to the Grade Analyzer!\n")
   
    # TODO (TASK 1): Call get_valid_grade() and display the result by uncommenting
    grade = get_valid_grade()
    print(f"Valid grade entered: {grade}")
   
    # TODO (TASK 2): Test is_eligible_for_honour_roll() with multiple cases by uncommenting
    print("\n--- Testing honour Roll Eligibility ---")
    grd = float(input("Student's grade (0-100): "))
    attendance = float(input("Student's attendance percentage (0-100): "))
    incidents = int(input("Number of behavioral incidents: "))
    result = is_eligible_for_honour_roll(grd,attendance,incidents )
    print (f"{result}")
    # Test at least 3 different scenarios
   
    # TODO (TASK 3): Call process_grade_file() by uncommenting
   
    print("\n--- Processing Grade File ---")
    process_grade_file("grades.txt", "grade_report.txt")
   


if __name__ == '__main__':
    main()











