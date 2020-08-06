## <div align="center"><img align="center" width="54px" src="/src/images/icon.png" /><br>Argila Parser<br>![version 2.0.0](https://img.shields.io/badge/version-2.0.0-blue.svg?style=flat-square)</div>

<br>

#### What is it?  
It's a lightweight object oriented lib for Python 3.8+ to help create CLI programs more easily. It has and elegant design taking advantage of built-in modules, and delivering a conducive environment to fast development and readability.  

<br>

#### Quickstart
This is the basic structure of your program, the class `App` represents the application, and the methods within it are the commands.  

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

**>** *<u>name</u>*\*: The name of the command used to call it. (This is the only nomination that matters, the method can have any name you'd like)  

**>** *<u>positional</u>*: A dict with all the positional arguments, the `key` should have the same name as the actual parameter in the method; the `value` is a short description of it. You invoke this argument with `--key value`.  

**>** *<u>optional</u>*: Same as positional, but optional arguments are **not** obligatory. You invoke this argument with `--key value`.  

**>** *<u>keyword</u>*: Same as positional, but keyword arguments are **not** obligatory and work as flags (bools). You invoke this argument with `--key`.  

The order in which you invoke each argument does **not** matter, as long as you keep the syntax `--key value`. The examples `add --a 1 --b 2` and `add --b 2 --a 1` are both correct.  

<br>

#### Development
In the process of adding `--help` and `--version` built-in commands.  
