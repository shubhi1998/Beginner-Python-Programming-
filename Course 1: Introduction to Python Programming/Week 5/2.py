max = None
min = None
while(True):
    num = input("Enter the number :")
    if num =="Done":
        break
    num = int(num)
    if max is None or num > max:
        max = num
    if min is None or num < min:
        min = num

print("Done printing")
print("Maximum :",max)
print("Minimum :",min)
