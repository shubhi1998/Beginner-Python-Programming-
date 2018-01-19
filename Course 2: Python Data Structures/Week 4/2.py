count = dict()
fhand =open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if line.startswith("From"):
        words =line.split()
        if len(words)>2:
            count[words[2]]= count.get(words[2],0)+1


print(count)
