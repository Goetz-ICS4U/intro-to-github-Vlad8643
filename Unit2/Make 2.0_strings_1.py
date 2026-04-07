"""
author: Vlad
date: 04.07.2026
"""


# Here are some useful string methods
# s.islower() – Returns True if all letters are lowercase, False otherwise.
# s.isupper() – Returns True if all letters are uppercase, False otherwise.
# s.istitle() – Returns True if the first letter of each word capitalized, False otherwise
# s.isdigit() – Returns True if all characters are numeric, False otherwise.
# s.isalpha() – Returns True if all characters are alphabetic, False otherwise.
# s.isalnum() – Returns True if all characters are letters or numbers, False otherwise.
# s.isspace() – Returns True if all characters are whitespace, False otherwise.

#12333


def example_1():
    word = "start"
    while word!= "":
       
            word = (input("Enter your word: "))
            if word == "":
                break
   
            #a
            first_letter = word[0]
            last_letter = word[-1]
            #b
            every_other = word[::2]
            #c
            palindrome = (word == word[::-1])
            #d
            if word.isalpha():
                answer="Composition: Entirely letters"
            elif word.isdigit():
                answer = "Composition: Entirely numbers"
            else:
                answer = "Composition: Mixed"
            #e
            count = 0  
            for char in word:
                 if not char.isalnum():
                    count += 1
            # f
            lower_c = 0
            upper_c = 0
            for char in word:
                if char.islower():
                    lower_c += 1
            if char.isupper():
                upper_c += 1
       
            print(f"First letter = {first_letter} and last letter is {last_letter}"
                  f"\nEvery other letter = {every_other}"                          
                  f"\nIs the word a palindrome? = {palindrome}"
                  f"\nGiven string is either composed entirely of numbers, or entirely of letters = {answer}"
                  f"\nNumber of  non-alphanumeric characters = {count} "
                  f"\nNumber of capital:{upper_c} and lowercase letters: {lower_c} ")
           

def example_2():
    while True:
        word = input("Enter your word #2: ")
        if word == "": break
        #a
        charinpython = 0
        char_to_check = input("Enter a letter to check in python': ")
        for char in char_to_check:
            if char in "python":
                charinpython +=1
            else:
                charinpython +=0
   
        #b 
        vowels = "aeiou"
        prev_char = ""
        doubles =0
        for char in word.lower():
            if char in vowels and char == prev_char:
                doubles += 1
            prev_char = char
        #c 
        vowels_up ="AEIOU"
        upper_count = 0
        for char in word:
            if char in vowels_up:
                    upper_count += 1
            else:
                    upper_count += 0
        #d
        prefix_suffix=  word.startswith("un") and word.endswith("ing")
        #e
        new_string = "".join(char for char in word if char.isalpha())
        #f
        temp_word = word.lower()
        ana_count = 0
        target = "ana"
        for i in range(len(temp_word) - 2):
            if temp_word[i : i + 3] == target:
                ana_count +=1
        #g
        n_inputs = int(input("How many integers for pandigital check? "))
        pan_total = 0

        for _ in range(n_inputs):
            num_str = input("Enter an integer: ")
            n = len(num_str)
            digits = []
            for char in num_str:
                digits.append(int(char))
            digits.sort()
            perfect_list = []
            for i in range(1, n + 1):
                perfect_list.append(i)
            if digits == perfect_list:
                pan_total += 1

        print(f"Number of pandigital integers entered = {pan_total}")

        print(f"a) Letters in 'python' = {charinpython}"
              f"\nb) Number of double vowels = {doubles}"
              f"\nc) Number of uppercase vowels = {upper_count}"
              f"\nd) Has prefix 'un' and suffix 'ing' = {prefix_suffix}"
              f"\ne) New string (letters only) = {new_string}"
              f"\nf) Number of 'ana' substrings = {ana_count}"
              f"\ng) Number of pandigital integers entered = {pan_total}")

example_1()
example_2()



