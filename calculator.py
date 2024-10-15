num1 = int(input("put your first number: ")) #variables for the two numbers
num2 = int(input("put your second number: "))
op = input("put the operator (+,-,*,/): ") #asks the user what kind of math problem
print(num1, op, num2)

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)