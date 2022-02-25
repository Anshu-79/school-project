
import statistics

"""here input has to be like a Python list ie must have square brackets
eval() is used to treat the str inside it as Python code"""
nums = eval(input("Enter a list of numbers: "))

n = int(input("Enter the number whose frequency you want: "))

mean = statistics.mean(nums)
f = nums.count(n)
"""If we can't use statistics, we can do something like:
mean = sum(nums)/len(nums)
"""

#giving output
print("The mean is", mean)
print("The frequency of", n, "is", f)
