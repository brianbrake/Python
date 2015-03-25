# Open the file romeo.txt and read it line by line:
# For each line, split the line into a list of words using the split() function. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

# romeo.txt file contains four lines of text(Romeo & Juliet: Act 2, Scene2):
#
# "But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief"


fname = raw_input("Enter file name: ")         # prompts user to type name of text file to read
fh = open(fname)                               
lst = list()                                   # creates empty list
for line in fh:
    words = line.split()                       # breaks four lines of text into four separate lists: words
    for word in words:                         # nested loop: reads each word from the four lists  
        if word in lst: continue
        lst.append(word)                       # builds single list of words from the four lists: e.g "['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks', 'It', 'is', 'the', 'east', 'and', 'Juliet', 'sun', 'Arise', 'fair', 'kill', 'envious', 'moon', 'Who', 'already', 'sick', 'pale', 'with', 'grief']"
lst.sort()                                     # alphabetical order
print lst 

# Expected output:  
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']


    
    

    
    
    
    
    
