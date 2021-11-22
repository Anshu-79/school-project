
myStr = input("Enter a string: ")

backwardStr = myStr[::-1]
print("Revered form:",backwardStr)


if myStr == backwardStr:
    print("Given string is a palindrome.")

elif myStr != backwardStr:
    print("Given string is not a palindrome.")
