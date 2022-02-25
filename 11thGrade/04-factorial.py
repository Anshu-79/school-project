
num = int(input("\nEnter number: "))
ans = 1

if num == 0 or num == 1:
  print(ans)

elif num > 1:
  for n in range(1, num+1):
    ans *= n
  print(ans)

else:
	print("Incorrect input. ValueError occured.")