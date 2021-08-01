'''
**********************************************************************************
@Author: Ayur Ninawe
@Date: 2021-07-31
@Last Modified by: 15:11:25 Ayur Ninawe
@Last Modified time: 2021-07-31
@Title : Reducer code for word length program
**********************************************************************************
'''

from operator import itemgetter
import sys
  
current_length = None
current_count = 0
word_length = None
# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word_length, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
  
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_length == word_length:
        current_count += count
    else:
        if current_length:
            # write result to STDOUT
            print ('%s\t%s' % (current_length, current_count))
        current_count = count
        current_length = word_length
  
# do not forget to output the last word if needed!
if current_length == word_length:
    print ('%s\t%s' % (current_length, current_count))