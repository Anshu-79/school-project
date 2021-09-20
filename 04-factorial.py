
num = int(input("\nEnter number: "))

try:
	if num == 0:
		ans = 1
		print(ans)

	elif num == 1:
		ans = 1
		print(ans)

	else:
		ans = 1
		for middle_nums in range(1, num+1):
			ans *= middle_nums
		print(ans)

except ValueError:
	print("Incorrect input. ValueError occured.")