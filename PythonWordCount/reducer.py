#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
'''
**********************************************************************************
@Author: Ayur Ninawe
@Date: 2021-07-27
@Last Modified by: 15:11:25 Ayur Ninawe
@Last Modified time: 2021-07-27
@Title : Reducer code for word count program
**********************************************************************************
'''


# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# slpiting the data on the basis of tab we have provided in mapper.py
	word, count = line.split('\t', 1)
	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if current_word == word:
		current_count += count
	else:
		if current_word:
			# write result to STDOUT
			print ('%s\t%s' % (current_word, current_count))
		current_count = count
		current_word = word

# do not forget to output the last word if needed!
if current_word == word:
	print ('%s\t%s' % (current_word, current_count))
