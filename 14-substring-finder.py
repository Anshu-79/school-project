
main_str = input("Enter a string: ")
sub_str = input("Enter a substring: ")

if sub_str in main_str:
    num = main_str.count(sub_str)

    print(num)
