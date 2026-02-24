import math

a = int(input("Please enter 1 number for check: "))
b = int(input("Please enter 2 number for check: "))
c = int(input("Please enter 3 number for check: "))

discriminant = math.sqrt((b**2) - (4*a*c))


eqpls = -b + discriminant // (2 *a )
eqmns = -b - discriminant // (2 *a )


if discriminant > 0:
    print(f"equation has 2  real solutoins {eqpls}  and  {eqmns}")

elif discriminant == 0:
    print(f"equation has 1 real solutoin {eqmns}")

else:
    print(f"equation has 0 real solutoin")

