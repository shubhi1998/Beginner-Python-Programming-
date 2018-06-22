Write a program to prompt for a file name, and then read through the
file and look for lines of the form:
X-DSPAM-Confidence:0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
the line to extract the floating-point number on the line. Count these lines and
then compute the total of the spam confidence values from these lines. then compute the total of the spam confidence values from these lines. 



CODE
filename = input("Enter the file name")
try:
    fhand = open(filename)
except:
    print("This file can't be printed")
    quit()
count =0
sum =0.0

for line in fhand:
    line = line.rstrip()




    if line.startswith("X-DSPAM-Confidence:"):

        atpos = line.find(":")
        spos = line[atpos+1:]
        sum = sum + float(spos)
        count=count+1
avg=sum/count
print"Average of confidence values: ",avg
