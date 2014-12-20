import unittest
from unittest_data import DataDecorator, data


@DataDecorator
class SampleTests(unittest.TestCase):

    @staticmethod
    def values():
        return (
            ('one', 1, int),
            ('two', 2, int),
            ('a', 'a', str),
            ('b', 'b', str),
        )

    @data('values', True)
    def types(self, value, type_):
        self.assertEqual(type(value), type_)


if __name__ == '__main__':
    unittest.main()
