'''
Created on 2014-12-19

@author: chenlei
'''
#!/usr/bin/python

# Filename: class_init.py

class Person:
    str = "First";
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hello, my name is', self.name
    
p = Person('Swarp')
p.str = 'PF'
p.sayHi();

q = Person('Test')
p.sayHi()
q.str = 'QF'
q.sayHi()

print 'QResult is', q.str
print 'PResult is', p.str


