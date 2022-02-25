lst = [1,2,7,27,37,47]
out_list = []
i = 0
elem = 0

for n in lst:
    while i <= lst.index(n):
        elem += lst[i]
        i += 1
    out_list.append(elem)

print(lst)
print(out_list)
