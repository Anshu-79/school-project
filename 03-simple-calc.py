
operations = {
	"+": "Adds the numbers",
	"-": "Finds difference in numbers",
	"*": "Multiplies the numbers",
	"/": "Divides the numbers",
	"//": "Divides the numbers and returns integer quotient",
	"**": "Raises one number to the other's power",
	"%": "Divides the numbers and returns remainder"
}

for operation in operations:
	print(operation, operations[operation])

chosen_op = input("\nEnter the symbol of desired operation: ")

a = float(input("\nEnter number one: "))
b = float(input("\nEnter number two: "))

try:
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

	elif chosen_op == "//":
		if b > a:
			print(b//a)
		else:
			print(a//b)

	elif chosen_op == "**":
		print(a**b)

	elif chosen_op == "%":
		if b > a:
			print(b%a)
		else:
			print(a%b)

	else:
		print("Incorrect input. ValueError occured.")

except ValueError:
	print("\nIncorrect input. ValueError occured.")

