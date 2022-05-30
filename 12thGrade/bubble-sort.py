
"""Code to take input list"""
nums = eval(input("Enter a list of numbers: "))

print("Inputted list: ", nums)


"""Bubble Sort Algorithm"""
swapped = True
while swapped == True:
    swapped = False

    # iterating till nums-1 only since we use the successor of every item anyway
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            # simple swap using tuple assignment
            nums[i], nums[i+1] = nums[i+1], nums[i]
            
            # making sure the loop executes one more time if there was a swap anywhere in the list
            swapped = True


print("Sorted list: ", nums)
