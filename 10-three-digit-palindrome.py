
num = int(input("Enter a three-digit number: "))

if len(str(num)) == 3:
    a = str(num)[0]
    b = str(num)[1]
    c = str(num)[2]

    output_str = c+b+a
    output = int(output_str)

    print(output)
    

else:
    print("Incorrect input")
