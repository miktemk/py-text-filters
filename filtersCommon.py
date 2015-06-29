import sys, os, re
import time, datetime
import getopt

def wholeWordOnly(text, x, y):
	if x == None or len(x) == 0:
		return text
	return re.sub(r"\b%s\b" % re.escape(x), y, text)