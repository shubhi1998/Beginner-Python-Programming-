counts= dict()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if line.startswith('From'):
        words = line.split()
        counts[words[1]]=counts.get(words[1],0)+1
bigcount = 0
bigword = None
for word,count in counts.items():
    if bigcount is 'None' or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, ":", bigcount)
