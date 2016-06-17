# !/usr/bin/python
import unittest
from unittest.mock import call, patch
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


class TestIntegration(unittest.TestCase):

    @patch('editor_grafico.input')
    @patch('editor_grafico.Matrix.create')
    def test_creation(self, mock_create, mock_input):
        """
        I M N
        Cria uma nova matriz MxN. Todos os pixels são brancos (O).
        """
        mock_input.side_effect = ('I 2 3', 'X')
        matrix = Matrix()
        matrix.app()
        self.assertTrue(mock_create.called)
        self.assertEqual(1, mock_create.call_count)
        self.assertEqual(call('2', '3'), mock_create.call_args)

    @patch('editor_grafico.input')
    @patch('editor_grafico.Matrix.create')
    def test_non_command(self, mock_create, mock_input):
        """
        Testar se um comando “aleatório” não cria matrix alguma
        """
        mock_input.side_effect = ('W 42', 'X')
        matrix = Matrix()
        matrix.app()
        self.assertFalse(mock_create.called)
        self.assertFalse(matrix.as_list)


if __name__ == '__main__':
    unittest.main()
