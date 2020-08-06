import typing
import unittest

from argila import Argila


@Argila.create
class App:
    @Argila.command(
        {
            'name': 'test_arguments_parse',
            'positional': {
                'a': 'Type string'
            },
            'optional': {
                'b': 'Type int'
            },
            'keyword': {
                'c': 'Type bool'
            }
        }
    )
    def test_arguments_parse(self, a: str, b: int=0, c:bool=False) -> typing.Tuple[str, int, bool]:
        return (a, b, c)


class Test(unittest.TestCase):
    def test_type_check(self) -> None:
        self.assertIsInstance(Argila.cast_args('str', str), str)
        self.assertIsInstance(Argila.cast_args('1', int), int)
        self.assertIsInstance(Argila.cast_args('1.5', float), float)
        self.assertIsInstance(Argila.cast_args('1', typing.Union[int, float]), int)
        self.assertTupleEqual(Argila.cast_args(['str', '1', '1.5', '1'], typing.Tuple[str, int, float, int]), ('str', 1, 1.5, 1))
        self.assertListEqual(Argila.cast_args(['1.3', '1.2', '9.5'], typing.List[float]), [1.3, 1.2, 9.5])

    def test_arguments_parse(self) -> None:
        argv = [__file__, 'test_arguments_parse', '--b', '1', '--c', '--a', 'string']
        a, b, c = Argila.run(debug=True, change_argv=argv)

        self.assertEqual(a, 'string')
        self.assertEqual(b, 1)
        self.assertEqual(c, True)
