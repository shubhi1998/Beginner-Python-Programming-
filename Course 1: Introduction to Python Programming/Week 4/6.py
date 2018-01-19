def computepay(hrs,r):
    if hrs>40:
        p= 40*r +(hrs-40)*1.5*r
    else:
        p = rate*hours
    return p
hours = float(input("Enter the number of hours:"))
rate =  float(input("Enter the rate :"))
Pay = computepay(hours,rate)
print("Pay: ",Pay)
