fhand = open('mbox-short.txt')
counter = 0


for line in fhand :
    line = line.strip()
    if not line.startswith('From '): continue
    words = line.split()
    print( words[1])
    counter +=1

print ("There were", counter, "lines in the file with From as the first word")
