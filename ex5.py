file_open = open("mbox-short.txt")

dct = {}
lst = list()

for line in file_open:
    line = line.split()
    if len(line) == 0: 
        continue 
    if line[0] != "From": 
        continue
    if line[5][:2] not in dct:
        dct[line[5][:2]] = 1
    else:
        dct[line[5][:2]] += 1


lst = list()
for val, key in list(dct.items()):
    lst.append((val, key))

lst.sort()

for val, key in lst:
    print(val, key)





