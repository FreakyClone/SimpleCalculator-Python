print("A simple calculator")

a = "+"
b = "-"
c = "/"
d = "*"
e = "Exit"

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
sum = input("Enter the operator you want to perform:")

if sum == a:
    print(num1+num2)

if sum == b:
    print(num1-num2)

if sum == c:
    print(num1/num2)

if sum == d:
    print(num1*num2)

