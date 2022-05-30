
inputStr = input("Enter a string: ")

backwardStr = inputStr[::-1]
print("Reversed form:",backwardStr)


if inputStr == backwardStr:
    print("Given string is a palindrome.")

elif inputStr != backwardStr:
    print("Given string is not a palindrome.")
