
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

choice = input("Which interest do you want to calculate?/nPress 1 for Simple Interest/nPress 2 for Compound Interest\t")

if choice == '1':
    interest = (principal * rate * time) / 100
    print(interest)

elif choice == '2':
    amount = (principal + (rate/100))**time
    interest = amount - principal
    print(interest)
