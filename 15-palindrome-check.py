
backStr = ''

myStr = input("Enter a string: ")

length = len(myStr)

i = length-1

while i >= 0: 
    backStr = backStr + myStr[i]
    i -= 1

print("Revered form:",backStr)


if myStr == backStr:
    print("Given string is a palindrome.")

elif myStr != backStr:
    print("Given string is not a palindrome.")

