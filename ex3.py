file_open = open("mbox-short.txt")
count = 0

for line in file_open:
    words = line.split()
    if len(words) ==0:
        continue
    if words[0] != "From:":
        continue
    count += 1
    print(words)

print("there are", count)

