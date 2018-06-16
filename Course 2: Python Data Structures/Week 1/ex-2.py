word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)

Encapsulate this code in a function named count, and generalize it so that it
accepts the string and the letter as arguments.

def count(line,let):
    count = 0
    for l in line :
        if l == let:
            count =  count + 1
    print(count)
word = 'banana'
letter = 'a'
count(word,letter)
