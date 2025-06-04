def calculator():
    print("🧮 Welcome to Simple Calculator!")

    try:
        # Take input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\n⚠️ Error: Division by zero is not allowed.")
        else:
            print("\n❌ Invalid operation choice.")

    except ValueError:
        print("\n❗ Please enter valid numbers.")

# Run the calculator
calculator()
