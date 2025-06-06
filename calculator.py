import sys

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        print(f"Result: {num1 * num2}")
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero")

# The code below will not be executed during a pytest
if __name__ == "__main__": 
    if len(sys.argv) != 4:
        print("Usage: calculator.py <num1> <num2> <operation>, please run again")
        sys.exit(1)

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]
    try:
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")
    except Exception as e:
        print("operators include <add> <subtract> <multiply> <divide>")
    