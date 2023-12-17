import math

t = float(input("Enter t: "))
x = float(input("Enter x: "))
denominator = math.sqrt(t) - abs(math.sin(t))

if denominator == 0:
    print("Error! Denominator is zero!")
else:
    z = ((9 * math.pi * t + 10 * math.cos(x)) / denominator) * math.e ** x
    print(f"Result is: {z:.2f}")
