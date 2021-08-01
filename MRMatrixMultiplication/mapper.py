'''
@Author: Ayur Ninawe
@Date: 2021-07-31
@Last Modified by: 15:11:25 Ayur Ninawe
@Last Modified time: 2021-07-31
@Title : Mapper code for matrix multiplication
'''

#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip() #used for removing white space
    entry = line.split(',') # splitting values by comma and storing it to entry
    key = entry[0]
    value = line[1:] 
    if key == "A":
        print('{0}\t{1}'.format(key,value))
    elif key == 'B':
         print('{0}\t{1}'.format(key,value))