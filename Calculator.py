print("===== BASIC CALCULATOR =====")

a = float(input("Enter first number: "))
opt= input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if opt == "+":
    print("Result:", a + b)

elif opt == "-":
    print("Result:", a - b)

elif opt == "*":
    print("Result:", a * b)

elif opt == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operator!")
