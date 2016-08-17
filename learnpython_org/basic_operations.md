## Basic Operators
### Arithmetic operators
```
number = 1 + 2 * 3 / 4.0
remainder = 11 % 3
square = 7 ** 2
cubed = 7 ** 3
```

Operators with strings
```
helloworld = "hello" + "" + "world"
lotsofhellos = "hello" * 10
```
Operators with lists
```
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers

prin [1, 2, 3] * 3
```
### string fomating 
like C-type string formatting
```
# This prints out "hello, John!"
name = "Hohn"
print "hello, %s!" % name
```
```
# This prints out "John is 23 years old."
name = "John"
age =23
print "%s is %d years old" %(name, age)
```
```
# This prints out: A list: [1, 2, 3]
mylist = [1, 2 ,3]
print "A list: %s" % mylist
```
```
%s - String (or any object with a string representation, like numbers)
%d - Intergers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount if digits to the right of the dot
%x/%X - Integers in hex representation(lowercase/uppercase)
```

### Basic string operations
```
astring = "Hello world!"
print "Single quotes are '"
print len(astring)
print astring.index("o")
print astring.count("l")
print astring[3:7]
print astring[3:7:1]
```
reverse a string like
```
print astring[::-1]
```
```
print astring.upper()
print astring.lower()
print astring.startswith("hello")
print astring.endswith("asfsfsfsf")
afewwords = astring.split(" ")
```
original: http://www.learnpython.org/en/Basic_Operators
