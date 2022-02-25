import math
print('''
	"ceil": "Returns the least integer greater than input",
	"floor": "Returns the greatest integer smaller than input",
	"pow": "Raises one number to the other's power",
	"sqrt": "Returns the square root of input"''')
func = input("\nType the code of the desired function: ")

if func == "ceil":
  num = float(input("Enter number to be ceiled: "))
  ans = math.ceil(num)
  print(ans)

elif func == "floor":
  num = float(input("Enter number to be floored: "))
  ans = math.floor(num)
  print(ans)

elif func == "pow":
  a = float(input("Enter base: "))
  b = float(input("Enter power: "))
  ans = math.pow(a, b)
  print(ans)

elif func == "sqrt":
  num = float(input("Enter number to be square-rooted: "))
  ans = math.sqrt(num)
  print(ans)

else:
  print("Incorrect input. ValueError occured.")