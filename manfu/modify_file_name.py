'''
Created on 2016-3-7

@author: chenlei
'''
import sys
import os

def renameFiles(currDir):
    files = os.listdir(currDir)
    
    for file in files:
        if os.path.isdir(file):
            renameFiles(file)
        else :
            filename = os.path.splitext(file)[0]
            sufix = os.path.splitext(file)[1]
            if ']' in filename:
                index = filename.index(']')
                fii = filename[index+1:]
                #os.chdir(currDir)
                srcfile = os.path.join(currDir, file)
                desfile = os.path.join(currDir, fii+sufix)
                try:
                    os.rename(srcfile, desfile)
                except Exception, ex:
                    print Exception, ":" , ex


currDir = os.path.dirname(__file__);
renameFiles(currDir)