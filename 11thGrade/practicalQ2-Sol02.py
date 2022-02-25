
import statistics

nums = input("""
Enter numbers seperated by a comma.
NOTE: Do not use spaces after commas
Enter numbers: """)

#changes nums type from str to list
nums = nums.split(',')

#changes datatype of every element in nums from str to float
for i in range(len(nums)):
    nums[i] = float(nums[i])

n = float(input("Enter the number whose frequency you want: "))

mean = statistics.mean(nums)
f = nums.count(n)

#giving output
print("The mean is", mean)
print("The frequency of", n, "is", f)
