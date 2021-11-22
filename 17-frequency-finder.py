
inpStr = input("""
You need to enter an array of numbers.
(Use commas without spaces to separate the numbers)
Your numbers: """)

inpList = inpStr.split(',')

inpSet = set(inpList)
#converted to set to remove duplicate items

for num in inpSet:
  print(num, "appears", inpList.count(num), "times.")
  
