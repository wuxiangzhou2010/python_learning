## Conditions

### Boolean operations
```
name = "John"
age = 23
if name == "John" and age == 23:
	print "Your name is John, and your are also 23 years old."

if name == "John" or name == "Rick":
	print "Your name is either John or Rick"
```

### The "in" operator
```
if name in ["John", "Rick"]:
	print "Your name is either John or Rick"
```
```
if <statement is true>:
	<do something>
	....
	....
elif <another statement is true>:
	<do something else>
	....
	....
else:
	<do another thing>
	....
	....
```
```
x = 2
if x == 2:
	print "x equals two"
else:
	print "x does not equal to two."
```
### The "is" and "not" operator
```
x = [1, 2, 3]
y = [1, 2, 3]

print x == y # Prints out true
print x is y # Prints out false
```
```
print not False
print (not False) == (False) # Prints out False
```
