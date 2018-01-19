hours = float(input("Enter hours:"))
rate = float(input("Enter rate:"))
if hours > 40:
    Pay = (40*rate) + (hours-40)*1.5*rate
else:
    Pay = hours *rate
print ("Pay :",Pay)
