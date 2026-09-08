def binary_calculator():
    def binary_to_decimal(binary):
        return int(binary, 2)

    def decimal_to_binary(decimal):
        return bin(decimal)[2:]

    print("Binary Calculator: Supports +, -, *, /")

    binary1 = input("First binary number: ")
    binary2 = input("Second binary number: ")
    operation = input("Operation (+, -, *, /): ")

    try:
        num1 = binary_to_decimal(binary1)
        num2 = binary_to_decimal(binary2)

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero.")
                return
            result = num1 // num2
        else:
            print("Invalid operation.")
            return

        print("Result in binary:", decimal_to_binary(result))
    except ValueError:
        print("Error: Invalid binary input. Please enter valid binary numbers.")

if __name__ == "__main__":
    binary_calculator()
