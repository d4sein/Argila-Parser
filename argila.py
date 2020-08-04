import typing
import sys


class Error(Exception):
    def __init__(self, error) -> None:
        sys.excepthook = lambda *exception: print(f'\n{error}\n')


class InvalidCommandError(Error):
    def __init__(self) -> None:
        error = 'Invalid command. \nCheck documentation for more info.'
        super().__init__(error)


class InvalidArgumentType(Error):
    def __init__(self, arg, typ) -> None:
        error = f'Invalid argument type given "{arg}", expected {typ}. \nCheck documentation for more info.'
        super().__init__(error)


class MissingItemInTuple(Error):
    def __init__(self) -> None:
        error = 'Missing item in argument of type tuple.'
        super().__init__(error)


class MissingPositionalArgumentError(Error):
    def __init__(self) -> None:
        error = 'Missing positional arguments.'
        super().__init__(error)


class Parser:
    def __init__(self):
        self.prefix = '--'
        self.commands = list()
        # Obligatory config values for commands
        self.obligatory = {'name'}

    def create(self, app: object) -> object:
        self.app = app
        return app

    def run(self) -> None:
        parsed = self.parse_argv()
        command, args = self.parse_command(parsed)
        # No error handling here, we don't want to omit useful errors for devs
        command(self.app, **args)

    def parse_command(self, parsed: dict) -> dict:
        command = [c for c in self.commands if c['name'] == parsed['name']][0]
        annotations = iter(command['annotations'])

        def cast_args(arg: str, typ: object) -> typing.Any:
            def cast_to(arg: str) -> typing.Union[int, float, str]:
                try:
                    return int(arg)
                except: pass

                try:
                    return float(arg)
                except: pass

                return arg # str

            if typ in (int, float, str):
                try:
                    return typ(arg[0])
                except:
                    raise InvalidArgumentType(arg[0], typ)

            if typ is typing.Any:
                return cast_to(arg[0])

            if typ.__origin__ is typing.Union:
                arg = cast_to(arg[0])

                if type(arg) in typ.__args__: return arg
                else: raise InvalidArgumentType(arg, typ.__args__)

            if typ.__origin__ is tuple:
                if len(arg) < len(typ.__args__): raise MissingItemInTuple()
                for i in range(len(arg)):
                    arg[i] = cast_args([arg[i]], typ.__args__[i])

                return arg

            if typ.__origin__ is list:
                for i in range(len(arg)):
                    arg[i] = cast_args([arg[i]], typ.__args__[0])
                return arg

        if positional := command.get('positional'):
            for arg in positional:
                try:
                    parsed_arg = parsed['args'][arg]
                except:
                    raise MissingPositionalArgumentError()
                else:
                    casted = cast_args(parsed_arg, next(annotations))
                    parsed['args'].update(
                        {
                            arg: casted
                        }
                    )

        if optional := command.get('optional'):
            for arg in optional:
                try:
                    parsed_arg = parsed['args'][arg]
                except:
                    pass
                else:
                    casted = cast_args(parsed_arg, next(annotations))
                    parsed['args'].update(
                        {
                            arg: casted
                        }
                    )

        if keyword := command.get('keyword'):
            for arg in keyword:
                try:
                    parsed_arg = parsed['args'][arg]
                except:
                    pass
                else:
                    parsed['args'].update(
                        {
                            arg: True
                        }
                    )

        return command['call'], parsed['args']

    def parse_argv(self) -> dict:
        parsed = dict(
            {
                'name': str(),
                'args': dict()
            }
        )

        if len(sys.argv) < 2: return # No command provided

        argv_command = sys.argv[1]
        # Checks if the given command exists
        if not list(filter(lambda command: command['name'] == argv_command, self.commands)): raise InvalidCommandError()

        parsed['name'] = argv_command

        args = sys.argv[2:]
        if not args:
            return parsed

        temp = []

        for arg in reversed(args):
            if arg.startswith(self.prefix):
                parsed['args'].update(
                    {
                        arg.strip(self.prefix): list(reversed(temp))
                    }
                )

                temp = []
            else:
                temp.append(arg)
        
        return parsed

    def command(self, config: dict) -> object:
        if not self.obligatory.issubset(set(config)):
            raise ValueError('Missing obligatory config values')

        def wrapper(func: object) -> object:
            annotations = list()

            for arg in func.__annotations__:
                if arg == 'return': continue

                annotations.append(func.__annotations__[arg])

            config.update(
                {
                    'call': func,
                    'annotations': annotations
                }
            )

            return func
        
        self.commands.append(config)
        return wrapper


Argila = Parser()
