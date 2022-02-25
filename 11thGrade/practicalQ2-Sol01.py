
import statistics

#exitLoop is False by default
exitLoop = False
nums = []

print("Type q to stop entering numbers")

#below while loop is executed till exitLoop is False
while exitLoop == False:
    try:
        n = input("Enter a number: ")

        if n == 'q':
            #exitLoop is only set to True when the user types q
            exitLoop = True

        else:
            nums.append(float(n))

    except ValueError:
        print("Incorrect input. Try again.")


print("The inputted list of numbers is", nums)

myNum = float(input("Enter number whose frequency you want: "))

mean = statistics.mean(nums)
f = nums.count(myNum)

#giving output
print("The mean is", mean)
print("The frequency of", myNum, "is", f)
