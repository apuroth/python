'''
Created on 2014-12-23

@author: chenlei
'''
#!/usr/bin/python
#Filename:inherit.py

class SchoolMember:
    ''' Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'Initialized SchoolMember:%s' % self.name
    def tell(self):
        ''' Tell my details.'''
        print 'Name: "%s" Age: "%s"' % (self.name , self.age),

class Teacher(SchoolMember):
    ''' Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'Initialized Teacher:%s' % self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    ''' Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'Initialized Student:%s' % self.name
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: %d' % self.marks
        
t = Teacher('Mr. Shrividya', 40, 4000)
s = Student('Sida', 21, 66)

print

members = [t, s]

for member in members:
    member.tell()