from argila import *


class Commands(Argila):
	'''This is a calculator'''
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

	@set_help({'a': 'First number', 'b': 'Second number', 'full_equation': 'Prints full equation'})
	@set_metavars({'a': 'n1', 'b': 'n2', 'full_equation': 'full'})
	def adds_two_numbers(a, b, full_equation=False) -> 'add':
		'''Adds two numbers'''
		if full_equation:
			print(f'{int(a)} + {int(b)} = {int(a) + int(b)}')
		else:
			print(int(a) + int(b))

	@set_help({'a': 'First number', 'b': 'Second number', 'n_times': 'Sets how many times the result should be printed'})
	@set_metavars({'n_times': 'repeat'})
	@set_optional_params(['n_times'])
	def subtracts_two_numbers(a, b, n_times) -> 'sub':
		'''Subtracts two numbers'''
		if n_times:
			for _ in range(int(n_times)):
				print(int(a) - int(b))
		else:
			print(int(a) - int(b))

	@set_help({'a': 'First number', 'b': 'Second number'})
	def divides_two_numbers(a, b) -> 'div':
		'''Divides two numbers'''
		print(int(a) / int(b))

	@set_help({'a': 'First number', 'b': 'Second number'})
	def multiplies_two_numbers(a, b) -> 'mul':
		'''Multiplies two numbers'''
		print(int(a) * int(b))


if __name__ == '__main__':
	Commands()
