### Introduction
> Argila is a class with methods that execute the logistics of arg parsing by pulling information from inheritance and decorators.
> It also relies on docstrings and annotations.

> To start, we need to import argila and create a class to add the commands and inherit from it.
```python
from argila import *


class Commands(Argila):
	def __init__(self):
		super().__init__(Commands)
```

> Now we can define the root, that is, the method that will contain substantial info about your program, using the `@root` decorator.  
> The underscore on `_root()` is how you tell Argila not to grab it as a command. You can name this method however you like, but I recommend keeping it default.  
```python
from argila import *


class Commands(Argila):
	def __init__(self):
		super().__init__(Commands)

	@root
	def _root():
		return {
		'head': 'This message will show at the top of your program',
		'version': 'Version 1.0.0',
		'greeting': 'Welcome!',
		'call': 'main.py'
		}
```
We can also call the class when the script is executed:
```python
if __name__ == '__main__':
	Commands()
```

There you go. Technically the program is already able to run.  

Now we can start adding commands.  
The `->` annotation is how you define the command name. In the first case, `adds_two_numbers()` will be called as `add`.  
Also, keep in mind that, at least for now, the args come raw from user input, that is, as strings, so you need to convert them first if you want them as int or float types. This will change in the near future, don't worry.
```python
from argila import *


class Commands(Argila):
	def __init__(self):
		super().__init__(Commands)

	@root
	def _root():
		return {
		'head': 'This message will show at the top of your program',
		'version': 'Version 1.0.0',
		'greeting': 'Welcome!',
		'call': 'main.py'
		}
		
	def adds_two_numbers(a, b) -> 'add':
		print(int(a) + int(b))

	def subtracts_two_numbers(a, b) -> 'sub':
		print(int(a) - int(b))
		
	def divides_two_numbers(a, b) -> 'div':
		print(int(a) / int(b))

	def multiplies_two_numbers(a, b) -> 'mul':
		print(int(a) * int(b))
		
		
if __name__ == '__main__':
	Commands()
```

That's pretty much it for the basics. You can check the rest of the [documentation][doc] for more advanced stuff.

[doc]: /doc/
