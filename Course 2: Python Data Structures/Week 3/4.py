fhand = open("romeo.txt")
word = list()
for line in fhand:
    line = line.strip()
    words = line.split()
    word.append(words)
count = list()
for w in word:
    if w not in count:
        count.append(w)
print("All the words:",word)
print("After removing the duplicates:",count)
