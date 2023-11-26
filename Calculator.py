class Calculator:

  @staticmethod
  def get_operation():
    while True:
      try:
        operation = input(
            "Enter the operation (add/subtract/multiply/divide/exit): ")
        break
      except ValueError:
        print("Invalid Input")
        continue
    return operation

  @staticmethod
  def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

  @staticmethod
  def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

  @staticmethod
  def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

  @staticmethod
  def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
      result = num1 / num2
      print(f"Result: {num1} / {num2} = {result}")
    else:
      print("Error: Division by zero")
