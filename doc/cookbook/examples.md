### Calculator

**code**  
```python
from argila import *


class Commands(Argila):
	def __init__(self):
		super().__init__(Commands)

	@root
	def _root():
		head = '''This is my calculator!
It can do a lot of things, like math.
Pretty cool, huh?'''

		return {
		'head': head,
		'version': 'Version 1.0.0',
		'greeting': 'Welcome!',
		'call': 'main.py'
		}

	@set_help({'a': 'First number', 'b': 'Second number'})
	@set_metavars({'a': 'n1', 'b': 'n2'})
	def adds_two_numbers(a, b) -> 'add':
		'''Adds two numbers'''
		print(int(a) + int(b))

	@set_help({'a': 'First number', 'b': 'Second number'})
	@set_metavars({'a': 'n1', 'b': 'n2'})
	def subtracts_two_numbers(a, b) -> 'sub':
		'''Subtracts two numbers'''
		print(int(a) - int(b))

	@set_help({'a': 'First number', 'b': 'Second number'})
	@set_metavars({'a': 'n1', 'b': 'n2'})
	def divides_two_numbers(a, b) -> 'div':
		'''Divides two numbers'''
		print(int(a) / int(b))

	@set_help({'a': 'First number', 'b': 'Second number'})
	@set_metavars({'a': 'n1', 'b': 'n2'})
	def multiplies_two_numbers(a, b) -> 'mul':
		'''Multiplies two numbers'''
		print(int(a) * int(b))	


if __name__ == '__main__':
	Commands()
```

**help message**
```
This is my calculator!
It can do a lot of things, like math.
Pretty cool, huh?

USAGE:
	main.py --help (command)

COMMANDS:
	-h, --help          Shows this message
	-a, --add           Adds two numbers
	-d, --div           Divides two numbers
	-m, --mul           Multiplies two numbers
	-s, --sub           Subtracts two numbers
 ```
