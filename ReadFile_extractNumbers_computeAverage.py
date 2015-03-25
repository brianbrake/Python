# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average
# Sample data at http://www.pythonlearn.com/code/mbox-short.txt
# Enter mbox-short.txt as the file name
# Expected output, "Average spam confidence: 0.750718518519"


# Request File from User; Open file
fname = raw_input("Enter file name: ")
fh = open(fname)

# Counter and Set num = 0
count = 0
num = 0

# Find String
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue      # If does't encounter text, continues with the next iteration of the loop
    
    # locate numbers between colon and end of string
    atpos = line.find(":")
    length = len(line)

    # Slice: colon+1 space to end of string
    # Remove whitespace between colon and number; convert string into number type float
    slicedText = float(line[atpos+1:length].rstrip())            

    # Find average   
    num = num + slicedText
    count = count +1
    average = num/count

print 'Average spam confidence:', average
  


