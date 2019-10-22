<img align="left" width="64px" src="/src/images/icon.png" />

# Argila-Parser  

### What is it?  
It's an asynchronous module written in Python 3.7 meant to help develop CLI programs more easily.  

### How does it work?  
It works by decorating your commands inside your Application class. Each decorator will take care of a specific setting, such as command name and aliases, and parameter types.  

The documentation is written on the module itself, import argila to access `argila.__DOC__`.

### How can I use it?  
Since this module runs asynchronously you need the asyncio library installed.
After that, simply add `argila.py` to your project's folder, import it to the main file, and you're good to go.  

### Quickstart:
```py
import asyncio

from argila import parser, command


class Application:
  parser.config()
  
  @command.positional({'name': 'The one to be greeted'})
  @command.name('greeting', aliases=['cumprimento'])
  async def greeting(self, name: str) -> None:
    '''Greets someone'''
    print(f'Hello, {name}.')
    

if __name__ == '__main__':
  asyncio.run(parser.run(Application))
```

### Goals  
In progress..  


###### If you want to support this project, please consider sharing this repo, giving it a star, fork or donating to:  
```
BTC: 19cCVv2esi5KroSgpja7kgdium8ixHwYxt  
ETH: 0xA5BAfed1094f087EcE37A6e5b7766317D408B2DC
```  
