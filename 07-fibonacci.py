
fibonacci_nums = [1, 1]
#This is the list of fibonacci numbers that we already know of

n = 2
#This is the position in fibonacci_nums from which we'll start entering numbers

upper_limit = 20
#The number of fibonacci numbers that we want

while len(fibonacci_nums) < upper_limit:
	new_num = fibonacci_nums[n-1]+fibonacci_nums[n-2]
	fibonacci_nums.append(new_num)
	n+=1

print(fibonacci_nums)
