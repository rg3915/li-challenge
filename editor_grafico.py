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

    def test_clean(self):
        """
        C
        Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam
        brancos (O).
        """
        self.matrix.create(2, 3, 'X')
        self.matrix.clean()
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

    def clean(self):
        for row_index, row in enumerate(self.as_list):
            for col_index, col in enumerate(row):
                self.as_list[row_index][col_index] = self.DEFAULT_VALUE


def main():
    pass


if __name__ == '__main__':
    unittest.main()
    main()
