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

    def test_colorize_pixel(self):
        """
        L X Y C
        Colore um pixel de coordenadas (X,Y) na cor C.
        """
        self.matrix.create(2, 3)
        self.matrix.colorize_pixel(1, 2, 'C')
        expected = [
            ['O', 'C', 'O'],
            ['O', 'O', 'O'],
        ]
        self.assertEqual(expected, self.matrix.as_list)

    def test_colorize_vertical_interval(self):
        """
        V X Y1 Y2 C
        Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2
        (intervalo inclusivo) na cor C.
        """
        self.matrix.create(2, 3)
        self.matrix.colorize_vertical_interval(2, 1, 2, 'C')
        expected = [
            ['O', 'C', 'O'],
            ['O', 'C', 'O'],
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

    def colorize_pixel(self, row, col, color):
        col, row = col - 1, row - 1
        self.as_list[row][col] = color

    def colorize_vertical_interval(self, col, line_start, line_end, color):
        for line in range(line_start, line_end + 1):
            index = line - 1
            self.as_list[index][col - 1] = color


def main():
    pass


if __name__ == '__main__':
    unittest.main()
    main()
