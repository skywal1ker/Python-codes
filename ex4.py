file_open = open("mbox-short.txt")

dct = dict()

for line in file_open:
    line = line.split()
    if len(line) == 0:
        continue
    if line[0] != "From:":
        continue
    #print(line[1])
    if line[1] not in dct:
        dct[line[1]] = 1
    else:
        dct[line[1]] += 1 
print(dct)

counts = None

for k, v in dct.items():
    if counts is None or counts < v:
        email = k
        counts = v
        
print("The most sender", email, counts)
