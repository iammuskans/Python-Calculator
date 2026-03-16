while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        print("\nWhat kind of operation do you want to perform?")
        print("Press + for addition")
        print("Press - for subtraction")
        print("Press * for multiplication")
        print("Press / for division")

        o = input("Enter Operation: ")

        match o:
            case "+":
                print(f"The result is: {a + b}")

            case "-":
                print(f"The result is: {a - b}")

            case "*":
                print(f"The result is: {a * b}")

            case "/":
                if b == 0:
                    print("Division by zero is not allowed.")
                else:
                    print(f"The result is: {a / b}")

            case _:
                print("Invalid operation.")

    except ValueError:
        print("Please enter valid numbers.")

    choice = input("\nDo you want to continue? (y/n): ").lower()

    if choice != "y":
        print("Calculator closed.")
        break