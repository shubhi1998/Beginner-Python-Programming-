import string
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst= list()
for key ,val in list(counts.items()):
    lst.append((val,key))
lst.sort(reverse =True)
for key,val in lst:
    print(key,val)
