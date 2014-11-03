#!/usr/bin/env python
# enable debugging
import os, sys
import urllib2
from StringIO import StringIO

def md2html(filename):
	print filename
	sys.path.append('pythoncms.com/Markdown-2.5')
	old_stdout = sys.stdout
	#sys.stdout = open('out.html', 'w')
	result = StringIO()
	sys.stdout = result
	

	if __name__ == '__main__':
	    sys.argv.append(filename)
	    from markdown.__main__ import run
	    run()

	sys.stdout = old_stdout
	result_string = result.getvalue()
	print (result_string)
	print filename
	#return result_string




