from Calculator import Calculator
from CalculatorMenu import CalculatorMenu


def main():
  calculator = Calculator()
  menu = CalculatorMenu()

  while True:
    menu.display_menu()
    operation = calculator.get_operation()

    if operation == "exit":
      print("Exiting the calculator. Goodbye!")
      break
    elif operation in ('add', 'subtract', 'multiply', 'divide'):
      getattr(calculator, operation)()
    else:
      print("Invalid operation. Please enter a valid operation.")


if __name__ == "__main__":
  main()
