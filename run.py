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
    def add(self, a: typing.List[int], b: typing.Union[int, float]) -> None:
        print(sum(a) + b)


if __name__ == '__main__':
    Argila.run()
