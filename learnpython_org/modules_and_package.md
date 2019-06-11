
# Modules and packages

```py
# import the library
import urllib

# use it
urllib.urlopen(...)
```

## Exploring built-in modules

  Two very important functions come in handy when exploring modules in Python - the dir and help functions.
  we can look for which functions are implemented in each module by using the dir function

```py
>>> import urllib
>>> dir(urllib)
>>> help(urllib.urlopen)
```

## Writing modules

## writing packages

```py
import foo.bar
# or
from foor import bar
```

```py
__init__.py
__all__ = ["bar"]
```

## random modulle

```py
import random
random.randint(0, 100)
random.randint(-10, 10) # negative number is ok too
```
