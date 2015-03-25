# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case
# Use the file words.txt to produce the output below
# Download the sample data at http://www.pythonlearn.com/code/words.txt


# Request File from User; Open file
fname = raw_input("Enter file name: ")
fh = open(fname)

# Read each line while capitalizing and removing line feeds (\n)
for line in fh:
    line = line.upper().rstrip()
    print line
    
