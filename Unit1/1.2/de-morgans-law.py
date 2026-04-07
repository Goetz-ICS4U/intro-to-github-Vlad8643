"""
author: Vlad
date: 03.23.2026
1.2 De morgans law
"""



## Question 1
x = int(input("Input your x value: "))
y = int(input("Input your y value: "))

if not (x > 10 and y < 5):
    print("inside the range")

else: 
    print("Outside the range")
# using de morgans law
if x<=10 or y>=5:
    print("inside the range")
else: 
    print("Outside the range")

## Question 2
player_level = 4
has_power_up = False

if player_level < 5 or not has_power_up:
    print("Level locked!")
else:
    print("good luck gamer")

#So this code check player's level and is it less than 5
#Also it checks the player does not have the required power-up
#if player fail even one of those tests he can not enter level

# Question 3
#on google doc

## Question 4
age = 25
is_student = False
is_senior = False

if age >=18 and not  is_student and age<65 and not is_senior:
    print("No discount available")
else:
    print("Discount available!")

## Question 5: 
is_logged_in = True
is_verified = True

if not(is_logged_in and is_verified):
    print("verified")

#Question 5
#- User must be logged in AND their account must be verified
# - Write a condition that checks if the user CANNOT post (using NOT with AND)
# - Then rewrite it using De Morgan's Law to check the same thing more clearly
# - Test your code with at least 3 different scenarios

logged_in = str(input("Did you logged in your account (True or False): "))
verified = str(input("Does your account verified (True or False): "))

if not( logged_in == "True" and verified == "True" ):
    print("Access not granted")
else:
    print("Access  granted")
if logged_in == "False" or verified == "False":
    print("Access not granted")
else:
    print("Access granted")