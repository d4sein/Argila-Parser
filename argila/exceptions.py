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
