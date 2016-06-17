# !/usr/bin/python
import unittest
from editor_grafico import Matrix


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


if __name__ == '__main__':
    unittest.main()
