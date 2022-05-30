filename = "Marks.dat"
file = open(filename, "r")

for i in file.readlines():
    print(i.rstrip('\n'))
