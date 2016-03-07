'''
Created on 2014-12-16

@author: chenlei
'''

#!/usr/bin/python
# filename: backup.py

import os
import time

source = ['~/test','~/build.txt']

target_dir = '/home/chenlei/'

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment: ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.tar.gz'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Success create directory', today

zip_command = "tar -zcvf %s %s" % (target, ' '.join(source))

print 'command is:', zip_command

if os.system(zip_command) == 0:
    print "Successful to:", target
else:
    print 'Backup FAILED'