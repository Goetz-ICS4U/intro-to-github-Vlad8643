"""
author: Vlad
date: 04.07.2026
"""

def example_1 ():
    #a
    text_1a = input ("Enter a string (max 10 chars): " )
    word_10= text_1a[:10]
    print(f"Left-justified: "+ word_10.ljust(20))
    print(f"Right-justified "+ word_10.rjust(20))
    print(f"Centered: "+ word_10.center(20))


    #1b
    s = input("Enter a string of As and Bs: ").upper()
    if all(char in "AB" for char in s.upper()):
        result = s.strip('Aa')
        print(f"Result:{result}")
    else:
            print("Error: The string must only contain As and Bs.")
    #  1c
    word = input("Enter letters only: ")
    if word.isalpha():
        result = word.strip('Aa')
        print(f"Result:{result}")
    else:
        print(" Only letters a-zare allowed.")
    #1d
    something = 1
    while something ==1:
        word = input("Enter a string of As and Bs: ")

        if all(char in "ABab" for char in word):
            count = 0
            something = 0
            
            for char in word:
                if char.upper() == 'A':
                    count += 1 
                else:
                    break

            if count % 2 == 0 and count > 0:
                result = word.lstrip('Aa')
                print(f"Even number of As removed:{result}")
            else:
                print(f"No As removed. Result:{word}")
        else:
            print("Error: Use only As and Bs.")
            something =1



def example_2 ():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    alpha_count = 0
    digit_count = 0


    for word in words:
        if word.isalpha():
            alpha_count += 1
        elif word.isdigit():
            digit_count += 1


    print(f"Words composed entirely of letters: {alpha_count}")
    print(f"Words composed entirely of digits: {digit_count}")


def isPalindrome(word):


    word = word.lower()
    return word == word[::-1] and len(word) > 1


def main():
    example_1()
    example_2()
    sentence = input("Enter a sentence to check for palindromes: ")
    words = sentence.split()
   
    found_any = False
    for w in words:
        if isPalindrome(w):
            print(f"'{w}' is a palindrome!")
            found_any = True
           
    if not found_any:
        print("No palindromes found in this sentence.")


if __name__ == "__main__":
    main()







