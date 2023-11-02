lastNumInInterval = int(input("Enter n: "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
interval = []
result = []

for i in range(lastNumInInterval + 1):
    interval.append(i)

if num1 not in interval and num2 not in interval and num3 not in interval:
    print("No number is in the range!")
else:
    if num1 in interval:
        result.append(num1)
    if num2 in interval:
        result.append(num2)
    if num3 in interval:
        result.append(num3)
    print(f'This number/numbers belong to the interval: {" ".join(map(str,result))}')