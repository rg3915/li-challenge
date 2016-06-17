# !/usr/bin/python


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

    def colorize_horizontal_interval(self, line, col_start, col_end, color):
        for col in range(col_start, col_end + 1):
            index = col - 1
            self.as_list[line - 1][index] = color

    def app(self):

        command_map = {
            'I': {
                'method': self.create,
                'args_min': 2,
                'args_max': 3,
                'error_message': 'Digite pelo menos dois números'
            }
        }

        while True:
            user_input = input('$ ')

            if user_input == 'X':
                break

            command_input, *args = user_input.split(' ')
            selected_command = command_map.get(command_input)
            if selected_command:
                cond1 = len(args) >= selected_command['args_min']
                cond2 = len(args) <= selected_command['args_max']
                if cond1 and cond2:
                    selected_command['method'](*args)
                else:
                    print(selected_command['error_message'])

if __name__ == '__main__':
    matrix = Matrix()
    matrix.app()
