
hours= input('Enter the number of hours worked: ')
rate =input('Enter the rate of hour: ')
try:
    hours = float(hours)
    rate = float(rate)
    if hours>40:
        Pay=(40*rate)+((hours-40)*1.5*rate)
    else:
        Pay= hours*rate

    print("Pay:",Pay)
except:
    print('\nError....!!!! Please enter a number')
