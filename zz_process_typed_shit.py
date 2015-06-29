import sys, os, re
import time, datetime
import getopt
from filtersCommon import wholeWordOnly

#print (wholeWordOnly("shit u ass", "u", "you"))
#print (re.sub(r'\bu\b', 'you', "shit u ass"))
optlist, args = getopt.getopt(sys.argv[1:], "")

# read file lines
fname = args[0]
if not os.path.exists(fname):
	print("File does not exist!!")
	
infile = open(fname, encoding="utf8")
text = infile.read()
#lines = infile.readlines() ### or read everything into array of lines
infile.close()

# replace the shortcuts
text = wholeWordOnly(text, "u", "you")
text = wholeWordOnly(text, "bc", "because")
text = wholeWordOnly(text, "Bc", "Because")
text = wholeWordOnly(text, "w/", "Because")
text = wholeWordOnly(text, "w/o", "Because")
text = wholeWordOnly(text, "diff", "difference")
text = wholeWordOnly(text, "diffs", "differences")
text = wholeWordOnly(text, "vs", "versus")
text = wholeWordOnly(text, "gonna", "going to")
text = wholeWordOnly(text, "thx", "thanks")
text = wholeWordOnly(text, "deg", "degrees")
text = wholeWordOnly(text, "degC", "degrees Celsius")
text = wholeWordOnly(text, "dev", "developpment")
text = wholeWordOnly(text, "info", "information")
text = wholeWordOnly(text, "temp", "temperature")
text = wholeWordOnly(text, "bw", "between")
text = wholeWordOnly(text, "EG", ", for example: ")
text = wholeWordOnly(text, "dont", "don't")
text = wholeWordOnly(text, "doesnt", "doesn't")

#fix any shit
text = text.replace(" ,", ",")
text = text.replace("., for example", ". For example")
text = text.replace(".\n, for example", ".\nFor example")
text = text.replace(".\r\n, for example", ".\r\nFor example")

# write to file
filename, fileExtension = os.path.splitext(fname)
fff = open(filename + "2.txt", "w", encoding="utf8")	
fff.write(text)
fff.close()
