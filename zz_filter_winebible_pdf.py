import sys, os, re
import time, datetime
import getopt

optlist, args = getopt.getopt(sys.argv[1:], "")

# read file lines
fname = args[0]
if not os.path.exists(fname):
	print("File does not exist!!")
	
infile = open(fname, encoding="utf8")
text = infile.read()
#lines = infile.readlines() ### or read everything into array of lines
infile.close()

text = text.replace("\r\n", "\n")

consonants = "BCDFGHJKLMNPQRSTVWXZbcdefghjklmnpqrstvwxzEOUeouyY"

# remove line with just numbers
text = re.sub(r"\n\d+\n", " ", text)

# remove text with too many suspicious characters in it
#text = re.sub(r"\n.*?\n\d+.*?\n", "\n\n", text)

# replace the shitty parts
text = text.replace("\\v", "w")

# write to file
filename, fileExtension = os.path.splitext(fname)
fff = open(filename + "2.txt", "w", encoding="utf8")	
fff.write(text)
fff.close()
