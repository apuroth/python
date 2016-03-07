#!/usr/bin/python

# Filename: use_list.py

# This is my shopping list

shoppinglist = ['apple', 'mango', 'banana']

print 'I have', len(shoppinglist), 'items to purchase.'

print 'These items are:'

for item in shoppinglist:
	print item
print '\nI alse have to buy rice.'
shoppinglist.append('rice')

print "My shoppinglist is now", shoppinglist
print "sort now"
shoppinglist.sort()

print 'Shopping list is', shoppinglist
print 'first', shoppinglist[0]
olditem = shoppinglist[0]
del shoppinglist[0]
print 'I bought the', olditem

print 'My shopping list is now', shoppinglist

test = (2,'tet')

test2 = (2)

print test
print test2