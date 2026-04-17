# Program: Student Report Card Analyzer
# Author: [Your Name]
# Purpose: To analyze student names, manage seating charts, and report on grades.

import copy

# ==================== BRONZE FUNCTION ====================

def analyze_name(full_name: str) -> tuple:
    """
    Cleans a student's name and extracts metadata.

    Args:
        full_name (str): The raw name string potentially including whitespace.

    Returns:
        tuple: (cleaned_name, word_count, vowel_count, initials)
    """
    # 1. Strip whitespace
    clean_name = full_name.strip()
    
    # 2. Split into words and get count
    name_split = clean_name.split()
    word_count = len(name_split)
    
    # 3. Count vowels (case-insensitive)
    vowels = "aeiou"
    vowel_count = 0
    for char in clean_name.lower():
        if char in vowels:
            vowel_count += 1
            
    # 4. Create initials
    first_letters = []
    for word in name_split:
        first_letters.append(word[0].upper())
    initials = "".join(first_letters)

    return (clean_name, word_count, vowel_count, initials)


# ==================== SILVER FUNCTION ====================

def build_seating_chart(rows: int, cols: int) -> tuple:
    """
    Creates a 2D seating chart and a backup copy.
    """
    chart = []
    
    # BUG 1: Appending the same 'row' variable makes all rows point to the same list memory.
    # FIX: Create a new list for each row inside the loop.
    for i in range(rows):
        chart.append(["empty"] * cols)

    chart[0][0] = "Alice"
    chart[1][2] = "Bob"

    # BUG 2: 'backup = chart' creates a reference, not a copy. 
    # FIX: Use deepcopy so changes to original 'chart' don't affect 'backup'.
    backup = copy.deepcopy(chart)

    # BUG 3: The original logic assigned 'backup' after Alice/Bob but then again later.
    # FIX: We ensure "Charlie" is added to 'chart' only AFTER the backup has been saved.
    chart[2][1] = "Charlie"

    return (chart, backup)


# ==================== GOLD FUNCTION ====================

def calculate_grade_report(grades: dict) -> tuple:
    """
    Processes a dictionary of student grades and returns a report.
    """
    # TODO: Implement this for Gold Tier
    pass


# ==================== MAIN ====================

def main() -> None:
    """Main function to run the Student Report Card Analyzer."""
    print("Welcome to the Student Report Card Analyzer!\n")

    # --- BRONZE ---
    # Input: User enters a name
    # Processing: analyze_name cleans and counts strings
    # Output: Formatted name data
    raw_input = input("Enter student full name: ")
    name, count, vowels, initials = analyze_name(raw_input)
    
    print(f"Cleaned Name: {name}")
    print(f"Word Count: {count}")
    print(f"Vowel Count: {vowels}")
    print(f"Initials: {initials}")

    # --- SILVER ---
    # Input: Row and Column dimensions (3x3)
    # Processing: build_seating_chart creates two independent 2D lists
    # Output: Prints original and backup charts
    print("\nBuilding Seating Chart...")
    orig_chart, back_chart = build_seating_chart(3, 3)

    print("Original Chart:")
    for row in orig_chart:
        print(f"  {row}")

    print("Backup Chart (should NOT have Charlie):")
    for row in back_chart:
        print(f"  {row}")


if __name__ == '__main__':
    main()