## Modules and packages
```
# import the library
import urllib

# use it
urllib.urlopen(...)
```
### Exploring built-in modules
  Two very important functions come in handy when exploring modules in Python - the dir and help functions.
  we can look for which functions are implemented in each module by using the dir function
```
>>> import urllib
>>> dir(urllib)
>>> help(urllib.urlopen)
```
### Writing modules
### writing packages
```
import foo.bar
# or 
from foor import bar
```
```
__init__.py
__all__ = ["bar"]
```
