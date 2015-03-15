# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'
# Once 'done' is entered, print out the largest and smallest of the numbers
# If the user enters anything other than a valid number catch it with a try/except w/ message & ignore the number


largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")  

    # Handle edge cases
    if inp == "done": break            # jumps out of loop if user types 'done'
    if len(inp) < 1 : break            # jumps out of loop if user hits enter key w/o input value
    
    #Do the work
    try:
        num=int(inp)                   # test for numerical values
    except:
        print 'Invalid input'
        continue                       # continues with the next iteration of the loop
    
    #Determine values
    if largest is None or num > largest:
        largest = num 

    if smallest is None or num < smallest:
        smallest = num
   
print "Maximum is", largest
print "Minimum is", smallest
       
       
