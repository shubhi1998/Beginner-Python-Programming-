filename = input("Enter the file name")
try:
    fhand = open(filename)
except:
    print("This file can't be opened")
    quit()
count =0
for line in fhand:
    line in line.rstrip()
    if not line.startswith("From"):
        continue
    words =line.split()
    print(words[1])
    count = count + 1
print "There were",count,"line in the file with From as the first word"
