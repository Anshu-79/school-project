
inp_string = input("Enter a string: ")

if inp_string.isalpha() == True:
    if inp_string.isupper() == True:
        print("Given string is all uppercase")

    elif inp_string.islower() == True:
        print("Given string is all lowercase")

elif inp_string.isdecimal() == True:
    print("Given string is all numbers")

elif inp_string.isspace() == True:
    print("Given string is all whitespace")

elif inp_string.isalnum() == True:
    print("Given string is a combination of lowercase, uppercase and numbers")


