def add_operation(number1, number2):
    addition_result = number1 + number2
    return addition_result

def sub_operation(number1, number2):
    subtraction_result = number1 - number2
    return subtraction_result

def multiplication_operation(number1, number2):
    multiplication_result = number1 * number2
    return multiplication_result

def division_operation(number1, number2):
    division_result = number1 / number2
    return division_result

while True:

     option = input("Please choose an operation: addition, subtraction, multiplication and division: ")

     if option != "addition" and option != "subtraction" and option != "multiplication" and option != "division":
         print("Invalid operation. Please choose one of the above mentioned: ")
         continue


     num1 = float(input("Please enter first number: "))
     num2 = float(input("Please enter second number: "))

     if option == "addition":
         print(add_operation(num1, num2))
     elif option == "subtraction":
         print(sub_operation(num1, num2))
     elif option == "multiplication":
         print(multiplication_operation(num1, num2))
     elif option == "division":
         print(division_operation(num1, num2))
     else:
         print("Unknown operation")
         exit()

