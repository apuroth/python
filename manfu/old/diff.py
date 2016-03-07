'''
Created on 2015-05-04

@author: chenlei
'''

#!/usr/bin/python
# filename: diff.py


base_path=''
source_file = '/home/chenlei/diff.txt'
des_file='/home/chenlei/test.txt'
#source_file = 'F:/diff.txt'
#des_file='F:/test.txt'
pstr = "[m"

sfp = open(source_file, "r")
dfp = open(des_file, "w")

for line in sfp:
    if pstr in line:
        nPos = line.index("[m")
        if (nPos > 0):
            base_path=line[12:nPos]
    else:
        if line.strip():
            dfp.write(base_path)
            dfp.write(line)
else:
    print 'The for loop is Over'
