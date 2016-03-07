#!usr/bin/python
# Filename: if.py

number = 22
running = True

while running:
	guess = int(raw_input('Enter an integer : '))

	if guess == number:
		print u'Congratulations!'
		running = False
	elif guess < number:
		print "It's a little highter than that"
	else:
		print "It's a little lower than that"
else:
		print 'The loop is OVER'
print 'Done'