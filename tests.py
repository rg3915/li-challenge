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

    def test_colorize_horizontal_interval(self):
        '''
        H X1 X2 Y C
        Desenha um segmento horizontal na linha Y nas colunas de X1 a X2
        (intervalo inclusivo) na cor C.
        '''
        self.matrix.create(2, 3)
        self.matrix.colorize_horizontal_interval(2, 1, 3, 'C')
        expected = [
            ['O', 'O', 'O'],
            ['C', 'C', 'C'],
        ]
        self.assertEqual(expected, self.matrix.as_list)

    def test_draw_rectangle(self):
        '''
        K X1 Y1 X2 Y2 C
        Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo
        e (X2,Y2) o canto inferior direito.
        '''
        self.matrix.create(4, 4)
        self.matrix.draw_rectangle(1, 1, 4, 4, 'C')
        expected = [
            ['C', 'C', 'C', 'C'],
            ['C', 'O', 'O', 'C'],
            ['C', 'O', 'O', 'C'],
            ['C', 'C', 'C', 'C'],
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

    @patch('editor_grafico.input')
    @patch('editor_grafico.Matrix.create')
    @patch('editor_grafico.print')
    def test_incomplete_command(self, mock_print, mock_create, mock_input):
        """
        Testar se um comando está incompleto
        """
        mock_input.side_effect = ('I 42', 'X')
        matrix = Matrix()
        matrix.app()
        self.assertFalse(mock_create.called)
        self.assertFalse(matrix.as_list)
        self.assertTrue(mock_print.called)


if __name__ == '__main__':
    unittest.main()
