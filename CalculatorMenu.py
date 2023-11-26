from colorama import Fore


class CalculatorMenu:

  def __init__(self):
    self.add_color = Fore.RED + "-add"
    self.mult_color = Fore.YELLOW + "-mult"
    self.sub_color = Fore.BLUE + "-sub"
    self.divi_color = Fore.MAGENTA + "-divi"

  def display_menu(self):
    print(f"""
Calculator Menu
---------------------------
{self.add_color} - Addition
{self.mult_color} - Multiplication
{self.sub_color} - Subtraction
{self.divi_color} - Division
---------------------------
""")
