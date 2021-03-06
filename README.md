## <div align="center"><img align="center" width="54px" src="https://raw.githubusercontent.com/d4sein/Argila-Parser/dev/src/images/icon.png" /><br>Argila Parser<br>![version 2.0.1](https://img.shields.io/badge/version-2.0.1-blue.svg?style=flat-square) ![pypi](https://img.shields.io/badge/pypi-pip_install_argilaparser-blue.svg?style=flat-square)</div>

<br>

#### What is it?  
It's a lightweight object oriented lib for Python 3.8+ to help create CLI programs more easily. It has an elegant design taking advantage of built-in modules, and delivering a conducive environment to fast development and readability.  

<br>

#### Quickstart
This is the basic structure of your program, the class `App` represents the application, and the methods within it are the commands.  

The `typing` module provides a built-in range of type hints, giving the developer a sophisticated way of accepting complex arguments. `Any, Union, Tuple, List` are currently supported.  

```py
import typing
from argila import Argila

@Argila.create
class App:
    @Argila.command(
        {
            'name': 'add',
            'positional': {
                'a': 'First element of the equation',
                'b': 'Second element of the equation'
            }
        }
    )
    def add(self, a: typing.Union[int, float], b: typing.Union[int, float]) -> None:
        '''This command adds two numbers together'''
        print(a + b)


if __name__ == '__main__':
    Argila.run()
```

A method is only considered a command if it has the `@Argila.command` decorator.  
Below is the configuration dict in its completeness.  

```py
{
    'name': 'command',
    'positional': {
        'a': 'Obligatory argument'
    },
    'optional': {
        'b': 'Optional argument'
    },
    'keyword': {
        'c': 'Keyword argument'
    }
}
```

***\*** means the key is obligatory.*  

**name\***: The name of the command used to call it. (This is the only nomination that matters, the method can have any name you'd like)  

**positional**: A dict with all the positional arguments, the `key` should have the same name as the actual parameter in the method; the `value` is a short description of it. You invoke this argument with `--key value`.  

**optional**: Same as positional, but optional arguments are **not** obligatory. You invoke this argument with `--key value`.  

**keyword**: Same as positional, but keyword arguments are **not** obligatory and work as flags (bools). You invoke this argument with `--key`.  

The order in which you invoke each argument does **not** matter, as long as you keep the syntax `--key value`. The examples `add --a 1 --b 2` and `add --b 2 --a 1` are both correct.  

<br>

Apart from it, the docstring `'''This command adds two numbers together'''` is how you set the description of a command. If not set, the description defaults to an empty string.  

<br>

Lastly, call `Argila.run()`, which is the method that will trigger all the subsequent others.  
