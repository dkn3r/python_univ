import math

x = float(input("Enter x: "))

if x >= 0:
    f = 0.5 - math.sqrt(abs(x))**1/3
    print(f"Result is: {f}")
else:
    f = (math.sin(x**2)**2)/abs(x+1)
    print(f"Result is: {f}")
