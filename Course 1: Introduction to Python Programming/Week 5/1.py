total=0.0
count = 0
while(True):
    num= input("Enter a number:")
    if num=="Done":
        break
    try:
            num = float(num)
    except:
           print("Invalid input")

    total+=num
    count = count + 1
print("\nDone counting")
avg = total/count
print(total ,count, avg)
