# Mutiple function argument
```
def myfunction(first, second, third)
	# do something with 3 variables
	...
```
```
def foo(first, second, third, *therest)
	print "First: %s" % first
	print "Second: %s" % second
	print "Third: %s" % third
	print "And all the rest... %s" % list(therest)
```
```
def bar(first, second, third, **options)
	if options.get("action") == "sum"
		print "The sum is: %d" % (first + second + third)

	if options.get("number") == "first"
		return first
result = bar(1, 2, 3, action = "sum", number = "first")
prit "Result %d" % result
```
