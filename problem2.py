import math


a = float(input("Enter number:"))
b = float(input("Enter number:"))
c = float(input("Enter number:"))

step1 = (b**2) - (4*a*c)
step2 = (-b-math.sqrt(step1))/(2*a)
print("The Quadratic formula has been solved! The answer is",(step2))
