counts =dict()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if line.startswith('From'):
        words = line.split()
        counts[words[1]]= counts.get(words[1],0)+1
print(counts)
