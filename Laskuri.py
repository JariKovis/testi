def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def ask():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    return num1, num2
while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break      
   elif user_input == "add":
      num1, num2 = ask() 
      result = str(add(num1,num2))
      print("The answer is " + result)
   elif user_input == "subtract":
      num1, num2 = ask() 
      result = str(subtract(num1,num2))
      print("The answer is " + result)
   elif user_input == "multiply":
      num1, num2 = ask() 
      result = str(multiply(num1,num2))
      print("The answer is " + result)
   elif user_input == "divide":
      num1, num2 = ask() 
      result = str(divide(num1,num2))
      print("The answer is " + result)
   else:
      print("Unknown input")
