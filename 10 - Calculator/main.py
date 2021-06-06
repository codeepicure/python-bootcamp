from art import logo

print(logo)

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

operations = {
  '+' : add,
  '-' : subtract,
  '/' : divide,
  '*' : multiply
}

def calculate(num1, num2, operation):
  return operations[operation](num1, num2)
  # if operation == "+":
  #   return add(num1, num2)
  # elif operation == "-":
  #   return subtract(num1, num2)
  # elif operation == "*":
  #   return multiply(num1, num2)
  # elif operation == "/":
  #   return divide(num1, num2)
  # else:
  #   print("Invalid operation")


should_continue_calculation = True
should_continue_program = False

first_num = int(input("Enter your first number? "))


while should_continue_calculation:

  second_num = int(input("Enter your second number? "))

  operation = input("Which operation would you like to perform (+,-,/,*)? ")

  result = calculate(first_num, second_num, operation)

  print(f"The result of the calculation is {result}.")
  should_continue = input("Would you like to proceed with this calculation? 'y/n' ")

  if should_continue == 'n':
    should_continue_calculation = False
  
  first_num = result



