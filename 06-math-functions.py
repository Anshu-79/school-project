import math

print("\n")
functions = {
	"ceil": "Returns the least integer greater than input",
	"floor": "Returns the greatest integer smaller than input",
	"pow": "Raises one number to the other's power",
	"sqrt": "Returns the square root of input"
}

for function in functions:
	print(function, functions[function])

chosen_func = input("\nType the code of the desired function: ")

try:
	if chosen_func == "ceil":
		num = float(input("Enter number to be ceiled: "))
		ans = math.ceil(num)
		print(ans)

	elif chosen_func == "floor":
		num = float(input("Enter number to be floored: "))
		ans = math.floor(num)
		print(ans)

	elif chosen_func == "pow":
		a = float(input("Enter base: "))
		b = float(input("Enter power: "))
		ans = math.pow(a, b)
		print(ans)

	elif chosen_func == "sqrt":
		num = float(input("Enter number to be square-rooted: "))
		ans = math.sqrt(num)
		print(ans)

	else:
		print("Incorrect input. ValueError occured.")

except ValueError:
	print("Incorrect input. ValueError occured.")

