'''
Created on 2014-12-16

@author: chenlei
'''

#!/usr/bin/python
# filename: backup.py

import os
import time

source = ['/home/chenlei/test','/home/chenlei/build.txt']

target_dir = '/home/chenlei/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" % (target, ' '.join(source))

print 'command is:', zip_command
if os.system(zip_command) == 0:
    print "Successful backup to", target
else:
    print 'Backup FAILED'