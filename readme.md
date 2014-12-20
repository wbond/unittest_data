# unittest_data

Data provider for unittest in Python. Some people may refer to these as test
generators.

This pair of class decorator and method decorator sets up a data provider for
a method and then generates new methods from the original.

The code is simple enough you can just grab `unittest_data.py` and drop it in
your project.

## Basic Usage

The `unittest.TestCase` class must be decorated with the `@DataDecorator` class
decorator.

For any test that you want to provide multiple sets of data to, leave off the
leading `test_` part of the name and add the `@data('provider')` decorator,
passing in the name of the class staticmethod to use as the data source.

*Using `@staticmethod` on the data source is only required for Python 2.*

```python
import unittest
from unittest_data import DataDecorator, data


@DataDecorator
class SampleTests(unittest.TestCase):

    @staticmethod
    def values():
        return (
            (1, int),
            (2, int),
            ('a', str),
            ('b', str),
        )

    @data('values')
    def types(self, value, type_):
        self.assertEqual(type(value), type_)


if __name__ == '__main__':
    unittest.main()

```

## Named Generated Test Method

By default the generated test method names are generated from the origin
decorated method, using incrementing integers as a suffix.

For instance, in the Basic Usage example, the generated method names would be:

 - `test_types_1()`
 - `test_types_2()`
 - `test_types_3()`
 - `test_types_4()`

If you would like to customize the names of these methods for easier debugging,
you can pass `True` as a second parameter to the `@data()` decorator. Then add
the generated test method name suffix as the first param of each set of data
coming from your provider.

It sounds more complicated than it is.

```python
import unittest
from unittest_data import DataDecorator, data


@DataDecorator
class SampleNamedTests(unittest.TestCase):

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

```

In this example, the generated test methods would be named:

 - `test_types_one()`
 - `test_types_two()`
 - `test_types_a()`
 - `test_types_b()`

## Tests

The tests have been run with python 2.6, 2.7, 3.3 and 3.4.

```bash
python tests.py
```

## License - Public Domain

The author or authors of this code dedicate any and all copyright interest in
this code to the public domain. We make this dedication for the benefit of the
public at large and to the detriment of our heirs and successors. We intend
this dedication to be an overt act of relinquishment in perpetuity of all
present and future rights to this code under copyright law.
