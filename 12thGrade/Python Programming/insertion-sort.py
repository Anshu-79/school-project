
"""Code to take input list"""
nums = eval(input("Enter a list of numbers: "))

print("Inputted list: ", nums)


"""Insertion Sort Algorithm"""
for i in range(1, len(nums)):
    
    n = nums[i]
 
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i-1
    while j >= 0 and n < nums[j] :
            nums[j + 1] = nums[j]
            j -= 1
    nums[j + 1] = n

print("Sorted list: ", nums)
