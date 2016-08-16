## Dictionaries
```
phonebook = {}
phonebook["john"] = 121212
phonebook["Jack"] = 343434
phonebook["Jill"] = 454545
```
```
phonebook = {
	"John" : 2122121,
	"jack" : 4343434,
	"Jill" : 9090898
}
```
### Iterating over dictionaries
```
for name, number in phonebook.iteritems():
	print "Phone numbers of %s is %d" %(name, number)
```

### Removing a value
```
del phonebook["John"]
```
or 
```
phonebook.pop("John")
```
