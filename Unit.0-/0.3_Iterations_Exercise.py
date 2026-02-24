"""
author: 
date: 
0.3 - Repetition Review Exercises
"""

# Task 1: Write a program to calculate the factorial of any number that the user enters using a loop. Ex. 5! = 5*4*3*2*1 = 120
# Your code goes here
n = int(input("Please input the number: "))
result = 1

while n > 0:
    result = result * n  
    n = n - 1            

print(f"The factorial is: {result}")


# Task 2a: Write a program that asks for five marks and computes the average, rounded to 1 decimal place.
# Your code goes here
marks_total = 0
n = 0 
for i in range (5):
    n += 1
    mark = int(input(f"Please input {n} mark: "))
    marks_total +=mark


av = marks_total /5 
print (f"Your mark avarage is: {av:.1f}")



# 2b)  Modify the program from task 2a to also output the lowest and highest mark WITHOUT lists.
# Your code goes here
lowest = 100
highest = -1  
marks_total = 0
n = 0 
for i in range (5):
    n += 1
    mark = int(input(f"Please input {n} mark: "))
    marks_total +=mark
    if  mark < lowest:
        lowest = mark
    if  highest > mark:
        highest = mark
   
 
    
av = marks_total /5 
print (f"Your mark avarage is: {av:.1f}")
print (f"The lowest mark is: {lowest:.1f}")
print (f"The highest mark is: {highest:.1f}")

# 2c)  Modify the program from task 2b to check if the mark entered is between 0 and 100. Keep asking user for input until they give a valid grade.
# Your code goes here



# 2d)  Modify the program to ask the user to enter -1 when done entering marks.
# Your code goes here





# Task 3a) Determine the largest of n positive integers entered the user.
# The program should loop until a negative value is read (aka, use Sentinel Value).
# Your code goes here



# 3b) Modify the program to find the two largest integers.
# Your code goes here




# Task 4) Use the random module to choose a number between 1 and 100.
# Then print all the factors of that number.
# Ask the user if they wish to play again – loop until the user enters “No” (sentinel value).
# Your code goes here
import random




# Task 5) One useful technique when analyzing a number is to use a loop and the modulus operator to extract each digit 
# from the end.
# Consider this code:

# num = int(input("Enter a positive integer: "))

#while (num >= 1):
 #   digit = num % 10
  #  num = num//10
   # print(digit)

# Use this above code to do the following:
# Count the number of sevens in a positive integer.




# Count the number of odd digits, and the number of even digits, in a positive integer.




