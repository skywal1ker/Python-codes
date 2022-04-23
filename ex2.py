file_open = open("romeo.txt")
lst = list()

for line in file_open:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
