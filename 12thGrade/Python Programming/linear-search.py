def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    

nums = eval(input("Enter a list of numbers: "))
n = int(input("Enter the number to be searched: "))

print("Index of",n,"in array =", linear_search(nums,n))
