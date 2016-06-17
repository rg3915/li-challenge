# !/usr/bin/python
import unittest


class TestUnit(unittest.TestCase):

    def setUp(self):
        self.matrix = Matrix()

    def test_create(self):
        """
        I M N
        Cria uma nova matriz MxN. Todos os pixels são brancos (O).
        """
        self.matrix.create(2, 3)
        expected = [
            ['O', 'O', 'O'],
            ['O', 'O', 'O'],
        ]
        self.assertEqual(expected, self.matrix.as_list)


class Matrix(object):

    DEFAULT_VALUE = 'O'

    def __init__(self):
        self.as_list = list()

    def create(self, rows, cols, default_value=None):
        rows, cols = int(rows), int(cols)
        default_value = default_value or self.DEFAULT_VALUE
        self.as_list = [[default_value] * cols for i in range(rows)]


def main():
    pass


if __name__ == '__main__':
    matrix = Matrix()
    main()
