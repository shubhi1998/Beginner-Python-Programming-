fhand = open('mbox-short.txt')
tot = 0.0
count = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        words = line.split()
        tot = tot + float(words[1])
        count = count + 1
print("Average spam confidence:",tot/count)
