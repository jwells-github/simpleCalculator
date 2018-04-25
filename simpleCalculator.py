# A program to complete the addition/subtraction/division/multiplication of two given numbers

#Tells the user how to use the program, and takes thair input
def start():
  global userInput, userInputSplit
  print('Please enter a Value, an Operator and another Value seperated by a single space \n' )
  print('e.g. 12 + 4')
  print('Type help for a list of operators')
  userInput = input()
  userInputSplit = userInput.split()

  if userInput == 'help':
    print('Use + for addition')
    print('Use - for subtraction')
    print('Use * for multiplication')
    print('Use / for division')
    start()

#Determines what operator the user entered and solves thier calculation
def solve(a,op,b):
  if op == '+':
    return str((a+b))
  elif op == '-':
    return str((a-b))
  elif op == '*': 
    return str((a*b))
  elif op == '/': 
    return str((a/b))
  else:
    return("Unrecognised Operator, please try again \n")

#Loops the program
while True:

  start()

  #Checks that the user entered a splittable string
  try:
    selectedOpeator = userInputSplit[1]
    #Checks that the user entered two numbers
    try:
      firstNumber = int(userInputSplit[0])
      secondNumber = int(userInputSplit[2])
    except:
      print("Your input wasn't a number, please try again \n")
      start()

  except:
      print("An error was encounterd, please ensure you have spaces between your numbers \n")
      start()

  #Returns the user's input and the solved answer for their input
  print(userInput + " = " + solve(firstNumber,selectedOpeator,secondNumber))
  print("\n")
