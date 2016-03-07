'''
Created on 2014-12-23

@author: chenlei
'''

#!/usr/bin/python
#FileName:objvar.py

class Person:
    ''' Represent a person.'''
    population = 0
    def __init__(self, name):
        ''' Initializes the person's data'''
        self.name = name
        print 'Initializing %s' %self.name
        
        #When this person is created, adds to population
        Person.population+=1
    def __del__(self):
        ''' I'm dying.'''
        print 'Say goodbye to', self.name
        Person.population -=1
        
        if Person.population==0:
            print 'It is last one.'
        else:
            print 'There are still %d people.' % Person.population
    def sayHi(self):
        ''' Greeting by the person.'''
        print 'Hi, it is %s.' % self.name
    def howMany(self):
        ''' Prints the current population.'''
        print 'We have %d persons here.' % Person.population
        
        
swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

kalam.sayHi()
kalam.howMany()

