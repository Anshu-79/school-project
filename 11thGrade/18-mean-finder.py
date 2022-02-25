import statistics

inpStr = input("""
You need to enter an array of numbers.
(Use commas without spaces to separate the numbers)
Your numbers: """)

inpList = inpStr.split(',')

#numbers were stored as str, so we change them to int
for i in range(len(inpList)):
  inpList[i] = int(inpList[i])
  

mean = statistics.mean(inpList)

print(mean)
