
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

choice = input('''Which interest do you want to calculate?
Press 1 for Simple Interest
Press 2 for Compound Interest\n''')

if choice == '1':
    interest = (principal * rate * t) / 100
    print(interest)

elif choice == '2':
    amount = (principal + (rate/100))**t
    interest = amount - principal
    print(interest)
