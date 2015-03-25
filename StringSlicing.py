# Write code using find() and string slicing to extract the number at the end of the line below:
# text = "X-DSPAM-Confidence:    0.8475"
# Convert the extracted value to a floating point number and print it out


text = "X-DSPAM-Confidence:    0.8475"
# Locate the colon within the string
atpos = text.find(':')

# Locate the end position of the string 
length = len(text)

#  Slice the string: one position after colon to the end
host = text[atpos+1:length]

#  Remove whitespace between colon and end of string; convert to number
print float(host.lstrip())




