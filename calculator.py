while True: 

    print("Select an operation to perform:")

    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")

    operation = input()

    if operation == "1":
        num1 = input("enter first number:")
        num2 = input("enter second number:")
        print("the sum is: " + str(int(num1) + int(num2)))
    elif operation == "2":
        num1 = input("enter first number:")
        num2 = input("enter second number:")
        print("the sum is: " + str(int(num1) - int(num2)))
    elif operation == "3":
        num1 = input("enter first number:")
        num2 = input("enter second number:")
        print("the sum is: " + str(int(num1) * int(num2)))
    elif operation == "4":
        num1 = input("enter first number:")
        num2 = input("enter second number:")
        print("the sum is: " + str(int(num1) / int(num2)))
    else:
        print ("Invalid Entry")

    again = input ("Go again? Y / N ")
    if again != "y":
        print("Goodbye")
        break