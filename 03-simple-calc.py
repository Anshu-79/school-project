print('''
"+": Adds the numbers
"-": Finds difference in numbers
'*': Multiplies the numbers
'/': Divides the numbers''')

chosen_op = input("\nEnter the symbol of desired operation: ")

a = float(input("\nEnter number one: "))
b = float(input("\nEnter number two: "))

if chosen_op == "+":
  print(a+b)

elif chosen_op == "-":
  if b > a:
    print(b-a)
  else:
    print(a-b)

elif chosen_op == "*":
  print(a*b)

elif chosen_op == "/":
  if b > a:
    print(b/a)
  else:
    print(a/b)

else:
  print("Incorrect input")