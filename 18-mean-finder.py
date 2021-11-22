import statistics

inpStr = input("""
You need to enter an array of numbers.
(Use commas without spaces to separate the numbers)
Your numbers: """)

inpList = inpStr.split(',')

for i in range(len(inpList)):
  inpList[i] = int(inpList[i])
  

mean = statistics.mean(inpList)

print(mean)
