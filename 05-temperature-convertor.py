
temp_code = input("Enter desired unit of temperature measurement: \nf = Fahrenheit\nc = Celcius\n").lower()

try:
	if temp_code == "f":
		inp_temp = float(input("Enter temperature in Celcius: "))

		temp = (inp_temp * 1.8) + 32
		print(temp)

	elif temp_code == "c":
		inp_temp = float(input("Enter temperature in Fahrenheit: "))

		temp = (inp_temp - 32) / 1.8
		print(temp)

except ValueError:
	print("Incorrect input. ValueError occured.")