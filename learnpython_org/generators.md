## Generators
```
import random

def lottery():
	# returns 6 numbers between 1 and 40
	for i in xrange(6):
		yield random.randint(1, 40)
	
	# return 1 7th number between 1 and 15
	yield random.randint(1, 15)

for random_numbers in lottery():
	print "And the next number i s... %d" % random_numbers
```
