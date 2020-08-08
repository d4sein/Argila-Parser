import sys


class Error(Exception):
    def __init__(self, error) -> None:
        sys.excepthook = lambda *exception: print(f'\n{error}\n\nUse "--help" for general info, or "command --help" for info on a specific command.\n')


class InvalidCommandError(Error):
    def __init__(self) -> None:
        error = 'Command doesn\'t exist or hasn\'t been called.'
        super().__init__(error)


class InvalidArgumentTypeError(Error):
    def __init__(self, arg, typ) -> None:
        error = f'Invalid argument type given for "{arg}", expected {typ}.'
        super().__init__(error)


class InvalidTupleArgumentError(Error):
    def __init__(self, expected, got) -> None:
        error = f'Incorrect amount of items given for type "tuple", expected {expected}, got {got}.'
        super().__init__(error)


class MissingPositionalArgumentError(Error):
    def __init__(self) -> None:
        error = 'Missing positional arguments.'
        super().__init__(error)
