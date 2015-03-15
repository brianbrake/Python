# Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours
# Put the logic to do the computation of time-and-a-half in a function called computepay()
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)


def computepay (hrs,rate):
    try:
        hrs=float(raw_input("Enter Hours: "))
        rate=float(raw_input("Enter Rate: "))
        if hrs <= 40:
            gross = hrs * rate
        else: 
            overtime = float (hrs-40)
            gross = (rate*40)+(overtime*1.5*rate)
        return gross
    except:
        print "Please type numerical data only.  Restart & try again:  "
        quit()
       
print computepay('hrs', 'rate')          
            
