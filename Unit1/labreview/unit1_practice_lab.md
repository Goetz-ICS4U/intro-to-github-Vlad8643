# Unit 0 Lab: Student Grade Analyzer

**Task**: You are building a student grade analyzer for Goetz that validates input, filters students, and processes grade files.

**Task 1**: 
You are given a broken function `get_valid_grade()` that currently crashes when users enter invalid input. Your job is to:
1. Add a **docstring** to the function
2. Fix the function to use **try/except**. Think about what kind of error will occur.
3. The function should keep asking until a valid grade (0-100) is entered
4. Once user inputs a valid grade, Return the grade
5. Call this function in `main()` to get a grade from the user and display it

### Sample Output
```
Welcome to the Grade Analyzer!

Enter a grade (0-100): hello
Invalid input. Please enter a number.
Enter a grade (0-100): -5
Grade must be between 0 and 100.
Enter a grade (0-100): 150
Grade must be between 0 and 100.
Enter a grade (0-100): 87.5
Valid grade entered: 87.5
```

---
**Task 2**: 
Write a function `is_eligible_for_honour_roll()` that returns `True` if a student qualifies for honour roll.

**Honour Roll Criteria** (student must meet ALL of these):
- Grade is 80 or higher
- Attendance is 90% or higher
- No behavioral incidents (incidents = 0)

Instead of checking:
```python
# DON'T do this (positive logic)
if grade >= 80 and attendance >= 90 and incidents == 0:
    return True
```
Apply **De Morgan's Law** to check the opposite (when student is NOT eligible):

### Sample Output
```
Welcome to the Grade Analyzer!

Enter a grade (0-100): 85
Valid grade entered: 85.0

Testing Honour Roll Eligibility
Student 1: Grade=85.0, Attendance=95%, Incidents=0
Eligible for Honour Roll: True

Student 2: Grade=75.0, Attendance=95%, Incidents=0
Eligible for Honour Roll: False

Student 3: Grade=85.0, Attendance=85%, Incidents=0
Eligible for Honour Roll: False

Student 4: Grade=90.0, Attendance=92%, Incidents=1
Eligible for Honour Roll: False
```

---
**Task 3**: Write a function `process_grade_file()` that:
1. Reads a file containing student names and grades (one per line: "Name,Grade")
2. Calculates the class average
3. Writes a new file with the results

**Requirements**:
- Use **try/except** to handle `FileNotFoundError` when reading the file. Use `except FileNotFoundError as e:` to capture the exception
- Use **try/except** to handle `ValueError` when parsing grades. Use `except ValueError as e:` to capture the exception
- Use **try/except** to handle `IOError` when writing the file. Use `except IOError as e:` to capture the exception
- If the input file doesn't exist, create a default file with sample data
- Write the output to a new file with class average and all student data

**File Format**:
- Input file (`grades.txt`):
  ```
  Alice,85
  Bob,92
  Charlie,78
  David,invalid
  Eve,95
  ```
- Output file (`grade_report.txt`):
  ```
  GRADE REPORT
  ============
  Alice: 85.0
  Bob: 92.0
  Charlie: 78.0
  David: ERROR - Invalid grade
  Eve: 95.0
  
  Class Average: 87.5
  Total Students: 4
  Invalid Entries: 1
  ```

### Sample Output
```
Welcome to the Grade Analyzer!

Enter a grade (0-100): 88
Valid grade entered: 88.0

--- Testing honour Roll Eligibility ---
Student 1: Grade=88.0, Attendance=95%, Incidents=0
Eligible for Honour Roll: True

--- Processing Grade File ---
Attempting to read 'grades.txt'...
File not found. Creating default file with sample data...
Default file 'grades.txt' created successfully.

Reading grades from 'grades.txt'...
Processed: Alice 
Processed: Bob
Processed: Charlie
Error: David
Processed: Eve 

Writing report to 'grade_report.txt'...
Report written successfully!

Summary:
- Total Students: 5
- Valid Grades: 4
- Invalid Entries: 1
- Class Average: 87.5
```

---

## Starter Code

```python
# ADD HEADER COMMENT


# ===================== TASK 1 FUNCTIONS =====================

def get_valid_grade():  # TODO: Add type annotation for return type
    """
    # TODO: Write a complete docstring
    # Should explain: what the function does, parameters, return value, 
    # and that it uses try/except to handle invalid input
    """
    # TODO: Implement this function using try/except
    grade = float(input("Enter a grade (0-100): "))
    return grade
    
    # HINTS:
    # - Use a while loop to keep asking until valid input
    # - Use try/except to catch ValueError
    # - Check if grade is between 0 and 100
    # - Return the valid grade as a float
    
    pass


# ===================== TASK 2 FUNCTION =====================

def is_eligible_for_honour_roll(grade: float, attendance: float, incidents: int) -> bool:
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
    
    pass


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
    
    pass


def create_default_grade_file(filename: str) -> None:
    """
    Creates a default grade file with sample student data.
    
    Args:
        filename (str): Name of the file to create
    """
    # TODO (Gold): Implement this helper function
    # Create a file with sample data like:
    # Alice,85
    # Bob,92
    # Charlie,78
    # David,invalid
    # Eve,95
    
    pass


# ===================== MAIN =====================

def main() -> None:
    """
    Main function that runs the grade analyzer.
    """
    print("Welcome to the Grade Analyzer!\n")
    
    # TODO (TASK 1): Call get_valid_grade() and display the result by uncommenting 
    # grade = get_valid_grade()
    # print(f"Valid grade entered: {grade}")
    
    # TODO (TASK 2): Test is_eligible_for_honour_roll() with multiple cases by uncommenting 
    # print("\n--- Testing honour Roll Eligibility ---")
    # Test at least 3 different scenarios
    
    # TODO (TASK 3): Call process_grade_file() by uncommenting 
    # print("\n--- Processing Grade File ---")
    # process_grade_file("grades.txt", "grade_report.txt")
    
    pass


if __name__ == '__main__':
    main()
```

---