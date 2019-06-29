## Documentation

- [Introduction](#introduction)  
- [Class Inheritance](#class-inheritance)  
- [Program settings](#program-settings)
- [Commands](#commands)
- [Docstrings and Annotations](#docstrings-and-annotations)  
- [Decorators](#decorators)  

### Introduction
Argila is a class with methods that take care of arg parsing by pulling information from inheritance and decorators. It also relies on docstrings and annotations to name commands, set help messages and other functionalities.

### Class Inheritance
By inheriting from Argila, your class is taken as an argument and used to access its methods, that subsequently are interpreted as commands. That's what the builtin function `super()` is for.
```python
from argila import *


class Commands(Argila):
	def __init__(self):
		super().__init__(Commands)
```

### Program Settings
The next step is to set some info about your program, like name and version. To do so, you need a *root* method.
```python
from argila import *


class Commands(Argila):
	def __init__(self):
    super().__init__(Commands)
    
	@root
	def _root():
		return {
		'head': 'This is my calculator!',
		'version': 'Version 1.0.0',
		'greeting': 'Welcome!',
		'call': 'main.py'
		}
```
The underscore on `_root()` is how you tell Argila not to grab it as a command. You can name this method however you like, but I recommend keeping it default.

`@root` is a decorator, it takes the decorated method as an argument.

The *return* statement returns a dict with all the info:

Key | Value
--- | ---
head | This will be shown at the top of your program's help message
version | Your program's current version
greeting | Your program's greeting message when ran without commands
call | How to run your program (not its name)

### Commands


### Docstrings and Annotations


### Decorators
