
s = input("Enter a string: ")

#initializing counter variables
uppers = 0
lowers = 0
alphabets = 0
digits = 0

for ch in s:
    if ch.isalpha():
        alphabets += 1
        
        #checking case of ch only after checking if it's an alphabet
        if ch.isupper():
            uppers += 1
        elif ch.islower():
            lowers += 1

    elif ch.isdigit():
        digits += 1

#giving output
print("Number of alphabets in",s,"=",alphabets)
print("Number of uppercase letters in",s,"=",uppers)
print("Number of lowercase letters in",s,"=",lowers)
print("Number of digits in",s,"=",digits)
