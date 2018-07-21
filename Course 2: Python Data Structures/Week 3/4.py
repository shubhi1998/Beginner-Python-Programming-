name = input("Enter the file name")
try:
    fhand = open(name)
except:
    print("This file can't be opened")
    exit()
lst= list()
for line in fhand:
    line = line.rstrip()
    words= line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
        else:
            continue
lst.sort()
print(lst)

