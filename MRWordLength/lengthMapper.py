'''
**********************************************************************************
@Author: Ayur Ninawe
@Date: 2021-07-31
@Last Modified by: 15:11:25 Ayur Ninawe
@Last Modified time: 2021-07-31
@Title : Mapper code for word length program
**********************************************************************************
'''

# import sys because we need to read and write data to STDIN and STDOUT
import sys
  
# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
      
    # we are looping over the words array and printing the word
    # with the count of 1 to the STDOUT
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print ('%s\t%s' % (len(word), 1))