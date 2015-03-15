# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error
# If the score is between 0.0 and 1.0, print a grade


try:
    iscore = raw_input("Enter Score between 0.0 and 1.0: ")
    score = float (iscore)
except:
    print 'Must be numerical score '
    quit('Re-read the directions; restart the programme!')
if score <0.0 or score>1.0:
    print 'error: Please follow directions & restart the programme' 
elif score >= 0.9:
    print 'A'
elif score >=0.8:
    print 'B'
elif score >=0.7:
    print 'C'
elif score >=0.6:
    print 'D'
elif score < 0.6:
    print 'F'
