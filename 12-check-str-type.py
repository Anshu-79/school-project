
inpStr = input("Enter a string: ")

if inpStr.isalpha():
    if inpStr.isupper():
        print("Given string is all uppercase")

    elif inpStr.islower():
        print("Given string is all lowercase")

elif inpStr.isdecimal():
    print("Given string is all numbers")

elif inpStr.isspace():
    print("Given string is all whitespace")

elif inpStr.isalnum():
    print("Given string is a combination of lowercase, uppercase and numbers")


