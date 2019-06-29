### Introduction
Argila is a class with methods that execute the logistics of arg parsing by pulling information from inheritance and decorators.
It also relies on docstrings and annotations.

To start, we need to create a class to add the commands, and inherit from Argila.
```python
class Commands(Argila):
	def __init__(self):
		super().__init__(Commands)
```

Now we can define the root, that is, the method that will contain substantial info about your program, using the `@root` decorator.  
The underscore on `_root()` is how you tell Argila not to grab it as a command. You can name this method however you like, but I recommend keeping it default.
```python
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
