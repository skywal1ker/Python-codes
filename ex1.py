open_file = open("mbox-short.txt")
#print(open_file)
total = 0
number = 0

for line in open_file:
    if line.startswith("X-DSPAM-Confidence:"):
        total += float(line[line.find(":") + 1 : len(line)])
        number += 1

print("average number", total/number)




