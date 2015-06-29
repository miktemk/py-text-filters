#USAGE: Drag and drop .sql backup-generated files onto this script.
# - adds on top:
#		drop schema `wordpress`;
#		CREATE SCHEMA `wordpress`;
#		use wordpress
# - replaces machine name PARTOUT!

import sys, os, re
import time, datetime
import getopt

BAD_MACHINE_NAME = "mkorikov"

optlist, args = getopt.getopt(sys.argv[1:], "")
alternameMachineName = raw_input("Instead of " + BAD_MACHINE_NAME + ": ")

for fname in args:
	infile = open(fname)
	#text = infile.read()
	lines = infile.readlines() ### or read everything into array of lines
	infile.close()
	fff = open(fname.replace(".sql", "_migratefix.sql"), "w")	
	fff.write("""
drop schema `wordpress`;
CREATE SCHEMA `wordpress`;
use wordpress;

""")
	for line in lines:
		line = line.replace(BAD_MACHINE_NAME, alternameMachineName)
		fff.write(line)
	fff.close()


