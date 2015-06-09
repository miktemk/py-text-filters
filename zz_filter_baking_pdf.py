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

consonants = "BCDFGHJKLMNPQRSTVWXZbcdefghjklmnpqrstvwxzEOUeouyY"

# replace the shitty parts
text = text.replace("ﬁ ", "fi")
text = text.replace("ﬂ ", "fl")
text = text.replace("ﬁ", "fi")
text = text.replace("ﬂ", "fl")
text = text.replace("A lthough", "Although")
text = text.replace("O ne", "One")
text = text.replace("A ll", "All")
for c in consonants:
	#text = text.replace(" " + c + " ", " " + c)
	for ii in range(40):
		text = text.replace(" " + c + " "*ii, " " + c)
		text = text.replace("\n" + c + " "*ii, "\n" + c)
		text = text.replace("\r" + c + " "*ii, "\r" + c)
text = text.replace("", " degrees ")
text = text.replace("", " degrees ")
text = text.replace("", ", more than ")
text = text.replace("", " times ")
text = text.replace("\r\n)\r\n", "\r\n\r\n")
text = text.replace("\n)\n", "\n\n")
text = re.sub(r"\n.*?\n\).*?\n", "\n\n", text)

# write to file
filename, fileExtension = os.path.splitext(fname)
fff = open(filename + "2.txt", "w", encoding="utf8")	
fff.write(text)
fff.close()
