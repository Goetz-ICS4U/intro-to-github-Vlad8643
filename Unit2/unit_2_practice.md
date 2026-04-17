# Unit 2 Practice Lab: Library Management System

## Task
You will create a library management system for your school library. The system needs to store book information, validate data, and provide various lookup and analysis features. You will practice working with strings, lists, tuples, and dictionaries.

---

### Task 1: Initialize the Library Catalog

Create a function `initialize_library()` that:
- Creates an empty dictionary called `library_catalog`
- Uses a loop to ask the user to input information for **at least 3 books**
- For each book, prompt for:
  - ISBN (e.g., "ISBN001")
  - Title
  - Author
  - Year published (as an integer)
  - Number of copies available (as an integer)
- Store each book as a dictionary with keys: "title", "author", "year", "copies"
- Add each book to the library_catalog using the ISBN as the key
- Returns the library_catalog dictionary

**Hint:** You can use a while loop and ask "Add another book? (yes/no)" or use a for loop with `range(3)` for exactly 3 books.

### Task 2: Search for a Book

Create a function `search_book(library_catalog, isbn)` that:
- Takes the library_catalog dictionary and an isbn string
- Uses `.get()` method to safely retrieve the book
- If found, prints the book information in a readable format with all fields
- If not found, prints "Book not found"
- Returns the book dictionary if found, or None if not found

### Task 3: Add New Book with Basic Validation

Create a function `add_book(library_catalog, isbn, title, author, year, copies)` that:
- Checks if the ISBN already exists (use `in` operator)
- If it exists, print "ISBN already exists in catalog" and return False
- Checks if year is between 1800 and 2025 (print error message if not)
- Checks if copies is greater than or equal to 0 (print error message if not)
- If all checks pass, adds the new book and prints "Book added successfully"
- Returns True if successful, False otherwise

### Sample Output
```
=== Initializing Library Catalog ===
Enter ISBN: ISBN001
Enter title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter year published: 1925
Enter number of copies: 3
Book added!

Add another book? (yes/no): yes

Enter ISBN: ISBN002
Enter title: To Kill a Mockingbird
Enter author: Harper Lee
Enter year published: 1960
Enter number of copies: 5
Book added!

Add another book? (yes/no): no

=== Searching for a Book ===
Enter ISBN to search: ISBN001

ISBN: ISBN001
Title: The Great Gatsby
Author: F. Scott Fitzgerald
Year: 1925
Copies Available: 3
```

---

### Task 4: ISBN and Title Validation

Create two validation functions:

**Function 1:** `validate_isbn(isbn)` that:
- Checks if the ISBN starts with "ISBN" (use `.startswith()`)
- Checks if the remaining characters after "ISBN" are all digits (use slicing and `.isdigit()`)
- Checks if the total length is at least 8 characters
- Returns `True` if valid, `False` if not

**Function 2:** `validate_title(title)` that:
- Checks if title is not empty (after stripping whitespace)
- Checks if title contains at least one letter (use `.isalpha()` on each character)
- Checks if title length is at least 1 character
- Returns `True` if valid, `False` if not

Update your `add_book()` function from Part 1 to use both validation functions before adding.

### Task 5: Search by Author

Create a function `search_by_author(library_catalog, author_name)` that:
- Takes an author name (case-insensitive search)
- Returns a list of tuples containing (isbn, title) for all books by that author
- Use `.lower()` for case-insensitive comparison
- Sort the list alphabetically by title before returning
- If no books found, return an empty list

### Task 6: Check Out Book

Create a function `checkout_book(library_catalog, isbn)` that:
- Checks if the ISBN exists in the library_catalog
- Checks if there are copies available (copies > 0)
- If available, decreases the copies by 1
- Prints "Book checked out successfully" with remaining copies
- Returns `True` if successful, `False` if book not found or no copies available
- Prints appropriate error messages

### Sample Output
```
=== Testing Validation ===
Testing ISBN: ISBN12345
Valid? True

Testing ISBN: 12345
Valid? False

Testing title: The Catcher in the Rye
Valid? True

Testing title: 
Valid? False

=== Searching by Author ===
Books by Harper Lee:
[('ISBN002', 'To Kill a Mockingbird')]

=== Checking Out Book ===
Checking out ISBN001
Book checked out successfully! 2 copies remaining.
```

---
### Task 7: Create Interactive Library Menu System

Create a function `display_menu()` that prints a menu and a function `main()` that runs the interactive system:

**The menu should display:**
```
=== Library Management System ===
1. Search for a book
2. Add new book
3. Check out a book
4. Return a book
5. Search by author
6. View library statistics
7. Find popular books
8. Exit
Enter your choice (1-8):
```

**Your `main()` function should:**
- Call `initialize_library()` at the start (with user input)
- Use a while loop to continuously show the menu until user chooses to exit
- Use if/elif statements to call the appropriate function based on user choice
- Handle invalid menu choices gracefully
- For each option, prompt for necessary inputs and display results
- Option 4 (Return a book) should increase the copies count by 1

### Task 8: Generate Library Statistics

Create a function `generate_statistics(library_catalog)` that:
- Calculates and returns a tuple containing (in this order):
  1. Total number of unique books (int)
  2. Total number of copies across all books (int)
  3. Average publication year (float, rounded to 1 decimal)
  4. Most common author (string - author with most books)
- In your menu option 6, use tuple unpacking to display these results in a formatted way

### Task 9: Group Books by Decade (No Aliasing!)

Create a function `group_by_decade(library_catalog)` that:
- Returns a dictionary where keys are decade strings (e.g., "1920s", "1960s", "2000s")
- Values are lists of book dictionaries published in that decade
- **CRITICAL:** Use proper copying techniques (`.copy()` method) to avoid aliasing issues
- Each book dictionary in the lists must be a separate copy, not a reference to the original
- Calculate decade by: `(year // 10) * 10` then format as string like "1920s"

**To prove no aliasing:** After grouping, modify one book in the grouped dictionary and show that the original library_catalog is unchanged. Include this test in your code with comments explaining what you're testing.

### Sample Output
```
=== Library Management System ===
1. Search for a book
2. Add new book
3. Check out a book
4. Return a book
5. Search by author
6. View library statistics
7. Find popular books
8. Exit
Enter your choice (1-8): 6

=== Library Statistics ===
Total unique books: 10
Total copies available: 47
Average publication year: 1978.5
Most prolific author: J.K. Rowling

Enter your choice (1-8): 8
Thank you for using the Library Management System!

--- ALIASING TEST ---
Original title: The Great Gatsby
Modified copy title: CHANGED TITLE
Are they the same? False
If False, no aliasing occurred!
```