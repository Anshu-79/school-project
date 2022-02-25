
inpStr = input("Enter a string: ")

alpha_count = 0
upper_count = 0
lower_count = 0
num_count = 0

for i in inpStr:
  if i.isalpha():
    alpha_count += 1

    if i.isupper():
      upper_count += 1
    
    elif i.islower():
      lower_count += 1

  elif i.isdecimal():
    num_count += 1

print("Alphabets: ", alpha_count)
print("Uppercase characters: ", upper_count)
print("Lowercase characters: ", lower_count)
print("Numbers: ", num_count)
  