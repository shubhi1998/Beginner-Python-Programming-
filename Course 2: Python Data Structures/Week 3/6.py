numbers = list()
while(True):
    num = input("Enter the number")
    if num =="Done":
        break
    try:
        num = int(num)
        numbers.append(num)
    except:
        print("Invalid number")
print("Maximum Number:",max(numbers))
print("Minimum Number:",min(numbers))
