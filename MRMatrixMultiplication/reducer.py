'''
@Author: Ayur Ninawe
@Date: 2021-07-31
@Last Modified by: 15:11:25 Ayur Ninawe
@Last Modified time: 2021-07-31
@Title : Reducer code for matrix multiplication
'''

#!/usr/bin/env python

import sys

matrixA = {}
matrixB = {}

for line in sys.stdin:
    line = line.strip() #used for removing white space
    key,value = line.split('\t') 
    v = value.split(',')

    if key == "A":
        matrixA[(int(v[1]),int(v[2]))] = int(v[3])
    elif key == 'B':
        matrixB[(int(v[1]),int(v[2]))] = int(v[3])

result = 0
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            result = result + matrixA[(i,k)]* matrixB[(k,j)]
        print('{0},{1}\t{2}'.format(i,j,result))
        result = 0