Write a while loop that starts at the last character in the string and
works its way backwards to the first character in the string, printing each letter on
a separate line, except backwards.




Code
line = 'banana'
index = len(line) - 1
while index >= 0 :
        letter = line[index]
        print(letter)
        index = index - 1
