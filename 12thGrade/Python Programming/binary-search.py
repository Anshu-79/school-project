def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if num < arr[mid]:
            end = mid-1
        elif num > arr[mid]:
            start = mid+1
        else:
            return mid
    else:
        return None

nums = sorted(eval(input("Enter a list of numbers: ")))
print("The sorted array is:", nums)

n = int(input("Enter the number to be searched: "))

print("Index of",n,"in sorted array =", binary_search(nums,n))
