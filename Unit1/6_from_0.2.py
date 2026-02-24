nCones = int(input("Please tell us how many cones did you sold:"))


if nCones >= 350:
    bonus = 45 + (nCones - 350) * 0.35 

elif nCones >= 250:
    bonus = 20 + (nCones - 250) * 0.25

elif nCones >= 150:
    bonus = 10 + (nCones - 150) * 0.10
    
if nCones < 150:
    print("You should sell more")
else:
    print(f"Your total bonus is: ${bonus:.2f}")