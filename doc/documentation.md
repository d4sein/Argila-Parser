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
*Thorough explanation on decorators further in the documentation.*

The *return* statement returns a dict with all the info:

Key | Value
--- | ---
head | This will be shown at the top of your program's help message
version | Your program's current version
greeting | Your program's greeting message
call | How to run your program

### Commands
Now you can start adding commands to your program, and it is as simple as creating a new method.
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
		
	def adds_two_numbers(a, b):
		print(int(a) + int(b))

	def subtracts_two_numbers(a, b):
		print(int(a) - int(b))
		
	def divides_two_numbers(a, b):
		print(int(a) / int(b))

	def multiplies_two_numbers(a, b):
		print(int(a) * int(b))
```
Argila has two builtin commands, `--version` and `--help`.  

Besides, there are 3 types of parameters you can have: *positional*, *optional* and *flags*.  
Positional parameters are necessary to run a command. For instance, `a` and `b` are positional params.  
Optional parameters aren't necessary, but can be called when running a command.  
To wrap it up, flags are bools, and are also not necessary. Their default value is False, and they always return True when called.  

*To use optional params you need to list them with `@set_optional_params` (see [decorators](#decorators) to now more).*  
*To use flags you need to set them to False in the method params, like so: `def command(flag=False) -> 'command':`*  

### Docstrings and Annotations
Docstrings and annotations are how you set command descriptions and names.  
Let's take `adds_two_numbers()`, for example:
```python
def adds_two_numbers(a, b) -> 'add':
	'''Adds two numbers'''
	print(int(a) + int(b))
```
`-> 'add'` is an annotation and it sets the command name.  
`'''Adds two numbers'''` is a docstring and it sets the command description.

This is the final product after adding docstrings and annotations to our code:
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
		
	def adds_two_numbers(a, b) -> 'add':
		'''Adds two numbers'''
		print(int(a) + int(b))

	def subtracts_two_numbers(a, b) -> 'sub':
		'''Subtracts two numbers'''
		print(int(a) - int(b))
		
	def divides_two_numbers(a, b) -> 'div':
		'''Divides two numbers'''
		print(int(a) / int(b))

	def multiplies_two_numbers(a, b) -> 'mul':
		'''Multiplies two numbers'''
		print(int(a) * int(b))
```

### Decorators
Decorators are how you tweak your commands and set new functionalities to them.  
See current list of decorators right below:

- ###### [set_help](#set_help)
- ###### [set_metavars](#set_metavars)
- ###### [set_optional_params](#set_optional_params)


### set_help  
description: It sets the description of a param to be displayed in the help message.  
usage: `@set_help({})`  
example:
```
@set_help({'a': 'First number', 'b': 'Second number'})
def adds_two_numbers(a, b) -> 'add':
	'''Adds two numbers'''
	print(int(a) + int(b))
```
result:  
`python main.py --help --add`  
```
USAGE:
	main.py --add a b

POSITIONAL ARGS:
	a                   First number
	b                   Second number
```

### set_metavars  
description: It sets a new name for a param.  
usage: `@set_metavars({})`  
example:  
```python
@set_metavars({'n_times': 'repeat'})
def adds_two_numbers(a, b, n_times) -> 'add':
	'''Adds two numbers'''
	for _ in range(int(n_times)):
		print(int(a) + int(b))
```
result:  
`python main.py --help --sub`  
```
USAGE:
	main.py --add a b repeat

POSITIONAL ARGS:
	a
	b
	repeat
```

### set_optional_params  
description: It sets optional params.  
usage: `@set_optional_params([])`  
example:  
```python
@set_optional_params(['n_times'])
def adds_two_numbers(a, b, to_the_power_of) -> 'add':
	'''Adds two numbers'''
	if n_times:
		print((int(a) + int(b)) ** int(n_times))
	else:
		print(int(a) + int(b))
```
result:  
`python main.py --help --add`  
```
USAGE:
	main.py --add a b [n_times]

POSITIONAL ARGS:
	a
	b

OPTIONAL ARGS:
	n_times
```
