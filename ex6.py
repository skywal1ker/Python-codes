smallest = 0
largest = 0
count = 0
attemps = 0


while True:
    num = input("Enter the number: ")
    if num == "done":
        break
    try:
        int_num = int(num)
    except:
        print("Invalid input, please truy again!")
        continue
    
    if largest == 0 or largest < int_num:
        largest = int_num
    if smallest == 0 or smallest > int_num:
        smallest = int_num
    count += int_num
    attemps += 1

print("--------------------------------------------------------------------")
print("This is the smallest:",smallest)
print("This is the largest:",largest)
print("You entered: ",attemps, "times")
print("Total amount: ",count, "times")
print("Average:", count/attemps)
print("--------------------------------------------------------------------")


