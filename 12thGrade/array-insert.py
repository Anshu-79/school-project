
nums = sorted(eval(input("Enter a list of numbers: ")))
print("The sorted array is:", nums)

n = int(input("Enter a number: "))

# Get index
for i in range(len(nums)):
    if nums[i] >= n:
        index = i
        break
    index = len(nums)
        
# Shift elements after index by 1 & insert n at index
nums.append(None)
for i in range(len(nums)-1, index-1, -1):
    nums[i] = nums[i-1]

nums[index] = n
print("The final array is:", nums)
