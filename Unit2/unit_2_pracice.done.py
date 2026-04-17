"""
Add your header comments here.
"""




# ============================
# PART 1: CORE FUNCTIONALITY
# ============================




def initialize_library() -> dict[str, dict[str, str | int]]:
    """
    Creates and returns a library catalog dictionary with user input.
    Prompts for ISBN, title, author, year, copies for at least 3 books.
    """
    library_catalog: dict[str, dict[str, str | int]] = {}




    answer= 0
    while answer !=1:
        isbn = input("Enter ISBN (e.g., ISBN001): ")
        title = input("Enter title: ")
        author = input("Enter author: ")
       
        year = int(input("Enter year published: "))
        copies = int(input("Enter number of copies: "))
       
       
        book_info = {
            "title": title,
            "author": author,
            "year": year,
            "copies": copies
        }
       
        library_catalog[isbn] = book_info
        print("Book added!\n")
        answer = input("Add another book? (yes/no): ").lower()
        if answer == 'no':
            answer = 1
           
    return library_catalog
   








def search_book(library_catalog: dict[str, dict[str, str | int]], isbn: str) -> dict[str, str | int] | None:
    """
    Searches for and displays a book by ISBN.
    Prints book info or "Book not found".
    """
    book = library_catalog.get(isbn)
   
    # 2. Проверяем, нашлась ли книга
    if book:
        # Если книга есть (то есть book не равно None)
        print(f"\nISBN: {isbn}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year: {book['year']}")
        print(f"Copies Available: {book['copies']}")
        return book
    else:
        # Если .get() вернул None
        print("Book not found")
        return None








def add_book(library_catalog: dict[str, dict[str, str | int]], isbn: str,
             title: str, author: str, year: int, copies: int) -> bool:
    """
    Adds a new book to the library catalog with basic validation.
    Checks if ISBN exists, validates year range and copies.
    Prints status message and returns True if successful, False otherwise.
    """
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Must start with 'ISBN', be 8+ chars, and end in digits.")
        return False
       
    if not validate_title(title):
        print("Invalid Title. Cannot be empty and must contain letters.")
        return False


    if isbn in library_catalog:
        print("ISBN already exists in catalog")
        return False
   
    if not (1800 <= year <= 2025):
        print("Error: Year must be between 1800 and 2025")
        return False
   
    if copies < 0:
        print("Error: Copies cannot be negative")
        return False
   
    # All checks passed
    library_catalog[isbn] = {
        "title": title,
        "author": author,
        "year": year,
        "copies": copies
    }
    print("Book added successfully")
    return True








# ============================
# PART 2: VALIDATION AND SEARCH FEATURES
# ============================




def validate_isbn(isbn: str) -> bool:
    """
    Validates ISBN format (must start with "ISBN" followed by digits, min length 8).
    """
    # TODO: Check if ISBN starts with "ISBN" using .startswith()
    # TODO: Check if length is at least 8
    # TODO: Check if characters after "ISBN" are all digits using slicing and .isdigit()
    if isbn.startswith("ISBN"):
        if isbn[4:].isdigit():
            if len(isbn) >=8:
                return True
    return False












def validate_title(title: str) -> bool:
    """
    Validates book title (not empty, contains at least one letter).
    """
    # TODO: Strip whitespace and check if not empty
    # TODO: Check if title contains at least one letter character
    # Hint: Loop through characters and use .isalpha()
    title_clean = title.strip()
    if len(title_clean) < 1:
        return False
    for ch in title_clean:
        if ch.isalpha():
            return True  
    return False




def search_by_author(library_catalog: dict[str, dict[str, str | int]], author_name: str) -> list[tuple[str, str]]:
    """
    Searches for all books by a specific author (case-insensitive).
    Returns sorted list of tuples (isbn, title).
    """
    results = []
    target_author = author_name.lower()
   
    for isbn, book in library_catalog.items():
        if book['author'].lower() == target_author:
            # Task 5 asks for a tuple of (isbn, title)
            results.append((isbn, book['title']))
           
    # TASK 5 FIX: Sort alphabetically by title (index 1 of the tuple)
    results.sort(key=lambda x: x[1])
    return results




def checkout_book(library_catalog: dict[str, dict[str, str | int]], isbn: str) -> bool:
    """
    Checks out a book (decreases copies by 1).
    Returns True if successful, False otherwise. Prints status message.
    """
    if isbn not in library_catalog:
        print("Book not found")
        return False
    book = library_catalog[isbn]
   
    if book['copies'] > 0:
        book['copies'] = book['copies'] - 1
        print(f"Book checked out successfully! {book['copies']} copies remaining.")
        return True
    else:  
        print("No copies available")
        return False








# ============================
# PART 3: INTERACTIVE SYSTEM AND ADVANCED FEATURES
# ============================




def display_menu() -> None:
    """
    Displays the library menu options.
    """
    print("\n=== Library Management System ===")
    print("1. Search for a book")
    print("2. Add new book")
    print("3. Check out a book")
    print("4. Return a book")
    print("5. Search by author")
    print("6. View library statistics")
    print("7. Find popular books")
    print("8. Exit")








def return_book(library_catalog: dict[str, dict[str, str | int]], isbn: str) -> bool:
    """
    Returns a book (increases copies by 1).
    Returns True if successful, False otherwise. Prints status message.
    """
    # TODO: Check if ISBN exists in library_catalog
    # TODO: If exists, increase copies by 1 and print success message
    # TODO: Return True if successful, False otherwise
   
    if isbn in library_catalog:
        library_catalog[isbn]['copies'] += 1
        print(f"Book '{library_catalog[isbn]['title']}' returned. New total: {library_catalog[isbn]['copies']}")
        return True
   
    print("Error: ISBN not found in catalog.")
    return False








def generate_statistics(library_catalog: dict[str, dict[str, str | int]]) -> tuple[int, int, float, str]:
    """
    Generates statistics about the library catalog.
    Returns tuple (total_books, total_copies, avg_year, common_author).
    """
    # TODO: Calculate total number of unique books
    # TODO: Calculate total copies across all books
    # TODO: Calculate average publication year (round to 1 decimal)
    # TODO: Find most common author (author with most books)
    # Hint: Create a dictionary to count books per author
    # TODO: Return tuple with all statistics
   
    if not library_catalog:
        return (0, 0, 0.0, "None")


    total_unique_books = len(library_catalog)
    total_copies = sum(book['copies'] for book in library_catalog.values())
   
    # Calculate average publication year
    all_years = [book['year'] for book in library_catalog.values()]
    avg_year = round(sum(all_years) / total_unique_books, 1)


    # Find the most common author
    author_counts = {}
    for book in library_catalog.values():
        auth = book['author']
        author_counts[auth] = author_counts.get(auth, 0) + 1
   
    # max() finds the author string with the highest count value
    common_author = max(author_counts, key=author_counts.get)


    return (total_unique_books, total_copies, avg_year, common_author)








def group_by_decade(library_catalog: dict[str, dict[str, str | int]]) -> dict[str, list[dict[str, str | int]]]:
    """
    Groups books by decade WITHOUT creating aliases.
    Returns dict {"1920s": [book_dicts], "1960s": [book_dicts], ...}
    """
    # TODO: Create empty dictionary for results
    # TODO: Loop through library_catalog.items()
    # TODO: Calculate decade: (year // 10) * 10, then format as "1920s"
    # TODO: For each book, create a COPY using .copy() method
    # TODO: Add the copy to the appropriate decade list
    # TODO: Return the grouped dictionary
   
    decade_results = {}
   
    for isbn, book_info in library_catalog.items():
        year = book_info['year']
        decade_str = f"{(year // 10) * 10}s"
   
        if decade_str not in decade_results:
            decade_results[decade_str] = []
        book_copy = book_info.copy()
        book_copy['isbn'] = isbn
        decade_results[decade_str].append(book_copy)
       
    return decade_results








def find_popular_books(library_catalog: dict[str, dict[str, str | int]], min_copies: int) -> list[tuple[str, str, int]]:
    """
    Finds books with at least min_copies available.
    Returns list of tuples (isbn, title, copies) sorted by copies descending.
    """
    # TODO: Create empty list for results
    # TODO: Loop through library_catalog.items()
    # TODO: If copies >= min_copies, add (isbn, title, copies) to list
    # TODO: Sort by copies in descending order
    # Hint: Use sorted() with key=lambda x: x[2], reverse=True
    # TODO: Return the sorted list
   
    results = []


    for isbn, info in library_catalog.items():
        # Use the key 'copies' directly from the dictionary
        count = info['copies']
       
        if count >= min_copies:
            # Create the tuple we need
            results.append((isbn, info['title'], count))
           
    # Sort using a lambda, but we can think of it as "sort by count"
    # x is the tuple (isbn, title, count)
    results.sort(key=lambda x: x[2], reverse=True)
   
    return results






def main() -> None:
    """
    Main function that runs the interactive library menu system.
    """
    print("Welcome to the Library Management System!")
    print("Let's initialize your library catalog.\n")
   
    # Initialize the library catalog with user input
    library_catalog: dict[str, dict[str, str | int]] = initialize_library()
   
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
       
        if choice == '1':
            isbn = input("Enter ISBN to search: ")
            search_book(library_catalog, isbn)
        elif choice == '2':
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            copies = int(input("Copies: "))
            add_book(library_catalog, isbn, title, author, year, copies)
        elif choice == '3':
            isbn = input("Enter ISBN to checkout: ")
            if checkout_book(library_catalog, isbn):
                print("Checkout successful.")
            else:
                print("Checkout failed (Check ISBN or availability).")
        elif choice == '4':
            isbn = input("Enter ISBN to return: ")
            return_book(library_catalog, isbn)
        elif choice == '5':
            author = input("Enter author name: ")
            results = search_by_author(library_catalog, author)
            print(f"Results: {results}")
        elif choice == '6':
            total, copies_count, avg, auth = generate_statistics(library_catalog)
            print(f"\n--- Statistics ---")
            print(f"Unique Books: {total}")
            print(f"Total Copies: {copies_count}")
            print(f"Avg Year: {avg}")
            print(f"Top Author: {auth}")
        elif choice == '7':
            min_c = int(input("Enter minimum copies: "))
            popular = find_popular_books(library_catalog, min_c)
            for item in popular:
                print(f"{item[1]} ({item[0]}): {item[2]} copies")
        elif choice == '8':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    print("\nThank you for using the Library Management System!")








# ============================
# TESTING CODE - DO NOT EDIT!
# ============================




def test_part1() -> None:
    """Test Part 1 functions."""
    print("=== PART 1 TESTS ===\n")
   
    # Test initialize_library
    library: dict[str, dict[str, str | int]] = initialize_library()
    print(f"\nInitialized {len(library)} books\n")
   
    # Test search
    if len(library) > 0:
        first_isbn: str = list(library.keys())[0]
        print(f"Searching for {first_isbn}:")
        search_book(library, first_isbn)
   
    # Test add
    print("\nTesting add_book:")
    result: bool = add_book(library, "ISBN999", "Test Book",
                           "Test Author", 2020, 5)
    print(f"Add successful: {result}")








def test_part2() -> None:
    """Test Part 2 functions."""
    print("\n=== PART 2 TESTS ===\n")
   
    # Test validation functions
    print("Testing validate_isbn:")
    print(f"  'ISBN12345': {validate_isbn('ISBN12345')} (should be True)")
    print(f"  '12345': {validate_isbn('12345')} (should be False)")
    print(f"  'ISBN1': {validate_isbn('ISBN1')} (should be False - too short)")
   
    print("\nTesting validate_title:")
    print(f"  'The Great Gatsby': {validate_title('The Great Gatsby')} (should be True)")
    print(f"  '': {validate_title('')} (should be False)")
    print(f"  '   ': {validate_title('   ')} (should be False)")
   
    # Create sample library for testing
    library: dict[str, dict[str, str | int]] = {
        "ISBN001": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
                    "year": 1925, "copies": 3},
        "ISBN002": {"title": "To Kill a Mockingbird", "author": "Harper Lee",
                    "year": 1960, "copies": 5},
        "ISBN003": {"title": "1984", "author": "George Orwell",
                    "year": 1949, "copies": 0}
    }
   
    # Test search by author
    print("\nTesting search_by_author:")
    books: list[tuple[str, str]] = search_by_author(library, "harper lee")
    print(f"  Books by Harper Lee: {books}")
   
    # Test checkout
    print("\nTesting checkout_book:")
    result1: bool = checkout_book(library, "ISBN001")
    print(f"  Checkout ISBN001: {result1} (should be True)")
    result2: bool = checkout_book(library, "ISBN003")
    print(f"  Checkout ISBN003: {result2} (should be False - no copies)")








def test_part3() -> None:
    """Test Part 3 functions."""
    print("\n=== PART 3 TESTS ===\n")
   
    # Create sample library
    library: dict[str, dict[str, str | int]] = {
        "ISBN001": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
                    "year": 1925, "copies": 3},
        "ISBN002": {"title": "To Kill a Mockingbird", "author": "Harper Lee",
                    "year": 1960, "copies": 5},
        "ISBN003": {"title": "1984", "author": "George Orwell",
                    "year": 1949, "copies": 2},
        "ISBN004": {"title": "Harry Potter", "author": "J.K. Rowling",
                    "year": 1997, "copies": 10},
        "ISBN005": {"title": "The Hobbit", "author": "J.R.R. Tolkien",
                    "year": 1937, "copies": 4}
    }
   
    # Test statistics
    print("Testing generate_statistics:")
    stats: tuple[int, int, float, str] = generate_statistics(library)
    if stats:
        total, copies, avg_year, author = stats
        print(f"  Total books: {total}, Total copies: {copies}")
        print(f"  Average year: {avg_year}, Most common author: {author}")
   
    # Test group by decade with aliasing check
    print("\nTesting group_by_decade (aliasing test):")
    grouped: dict[str, list[dict[str, str | int]]] = group_by_decade(library)
    if grouped:
        print(f"  Decades found: {list(grouped.keys())}")
        original_title: str = str(library["ISBN001"]["title"])
        # Try to modify a grouped copy
        if "1920s" in grouped and len(grouped["1920s"]) > 0:
            grouped["1920s"][0]["title"] = "CHANGED TITLE"
            print(f"  Original title: {library['ISBN001']['title']}")
            print(f"  Modified copy: {grouped['1920s'][0]['title']}")
            if original_title == library["ISBN001"]["title"]:
                print("  ✓ No aliasing! Original unchanged.")
            else:
                print("  ✗ Aliasing detected! Original was modified.")
   
    # Test find popular books
    print("\nTesting find_popular_books:")
    popular: list[tuple[str, str, int]] = find_popular_books(library, 4)
    if popular:
        print(f"  Books with 4+ copies:")
        for isbn, title, copies in popular:
            print(f"    {title}: {copies} copies")








if __name__ == "__main__":
    # Uncomment the tests you want to run:
   
    # For Part 1 testing:
    test_part1()
   
    # For Part 2 testing:
    test_part2()
   
    # For Part 3 testing:
    test_part3()
   
    # For Part 3 interactive menu:
    main()
   
    print("Uncomment the test functions or main() to run the program!")









# =========================================================
# ШПАРГАЛКА ПО ЛАБЕ: СТУДЕНТЫ (DICT + 2D LIST)
# =========================================================


# Исходные данные (2D список)
students_raw = [
    [101, "Ivan", "CS-01", 4.8],
    [102, "Maria", "CS-02", 5.0],
    [103, "Petr", "CS-01", 3.2]
]


# --- 1. ПЕРЕНОС ИЗ 2D СПИСКА В СЛОВАРЬ ---
def load_students(data_list):
    db = {}
    for row in data_list:
        # s_id будет КЛЮЧОМ, остальное — ЗНАЧЕНИЕМ (словарем)
        s_id = row[0]
        db[s_id] = {
            "name": row[1],
            "group": row[2],
            "gpa": float(row[3]) # Средний балл всегда float
        }
    return db




# --- 2. ФИЛЬТРАЦИЯ (ОТЛИЧНИКИ) ---
def get_honors_students(db, threshold=4.5):
    honors = []
    # Используем .items() чтобы видеть и ID, и данные студента
    for s_id, info in db.items():
        if info['gpa'] >= threshold:
            # Сохраняем кортеж (ID, Имя), чтобы не потерять связь
            honors.append((s_id, info['name']))
            
    # СОРТИРОВКА: по имени (индекс 1 в кортеже)
    honors.sort(key=lambda x: x[1])
    return honors




# --- 3. ПОИСК ПО ГРУППЕ ---
def find_by_group(db, group_name):
    # Быстрый способ собрать список имен через List Comprehension
    return [info['name'] for info in db.values() if info['group'] == group_name]




# --- 4. МАТЕМАТИКА (СРЕДНИЙ БАЛЛ ПО ВСЕМ) ---
def calculate_average_gpa(db):
    if not db: return 0.0
    
    # Собираем все gpa в один список и считаем среднее
    all_gpas = [info['gpa'] for info in db.values()]
    return round(sum(all_gpas) / len(all_gpas), 2)




# --- 5. ОБНОВЛЕНИЕ ДАННЫХ ---
def update_gpa(db, student_id, new_gpa):
    if student_id in db:
        db[student_id]['gpa'] = new_gpa
        return True
    return False




# --- 6. ПОИСК ЛУЧШЕГО (MAX) ---
def get_top_student(db):
    if not db: return None
    # Ищем во всех словарях-значениях тот, где gpa максимальный
    return max(db.values(), key=lambda x: x['gpa'])


# =========================================================
# КОРОТКИЙ ГАЙД:
# 1. db[101] -> {"name": "Ivan", "group": "CS-01", "gpa": 4.8}
# 2. db[101]['name'] -> "Ivan"
# 3. for s_id, info in db.items() -> стандарт для поиска.
# 4. info['gpa'] -> как достучаться до балла внутри цикла.
# =========================================================



