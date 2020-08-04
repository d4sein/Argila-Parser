<img align="left" width="64px" src="/src/images/icon.png" />

# Argila Parser  

#### What is it?  
It's an object oriented lib for Python 3 meant to help develop CLI programs more easily.  

---

#### Documentation
This is the basic structure of your app.
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
