filename = "Marks.dat"
file = open(filename,"w")

n = int(input("Enter number of lines to write: "))
for i in range(n):
    line = input("Content for line " + str(i+1) + ": ")
    file.write(line+'\n')

file.close()
