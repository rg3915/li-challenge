# !/usr/bin/python
class Matrix(object):

    DEFAULT_VALUE = 'O'

    def __init__(self):
        self.as_list = list()

    def create(self, cols, rows, default_value=None):
        rows, cols = int(rows), int(cols)
        default_value = default_value or self.DEFAULT_VALUE
        self.as_list = [[default_value] * cols for i in range(rows)]

    def clean(self):
        for row_index, row in enumerate(self.as_list):
            for col_index, col in enumerate(row):
                self.as_list[row_index][col_index] = self.DEFAULT_VALUE

    def colorize_pixel(self, row, col, color):
        col, row = int(col) - 1, int(row) - 1
        self.as_list[col][row] = color

    def colorize_vertical_interval(self, x, y1, y2, color):
        for y in range(int(y1), int(y2) + 1):
            index = int(y) - 1
            self.as_list[index][int(x) - 1] = color

    def colorize_horizontal_interval(self, x1, x2, y, color):
        for x in range(int(x1), int(x2) + 1):
            index = int(x) - 1
            self.as_list[int(y) - 1][index] = color

    def draw_rectangle(self, x1, y1, x2, y2, color):
        self.colorize_vertical_interval(x1, y1, y2, color)
        self.colorize_vertical_interval(x2, y1, x2, color)
        self.colorize_horizontal_interval(x1, x2, y1, color)
        self.colorize_horizontal_interval(x1, x2, y2, color)

    def colorize_region(self):
        pass

    @property
    def as_string(self):
        list_of_strings = [' '.join(c for c in line) for line in self.as_list]
        return '\n'.join(list_of_strings)

    def save(self, name):
        with open(name, 'w') as f:
            print(self.as_string, file=f)

    def app(self):

        command_map = {
            'I': {
                'method': self.create,
                'args_min': 2,
                'args_max': 3,
                'error_message': 'Digite pelo menos dois números'
            },
            'C': {
                'method': self.clean,
                'args_min': 0,
                'args_max': 0,
            },
            'L': {
                'method': self.colorize_pixel,
                'args_min': 2,
                'args_max': 3,
                'error_message': 'Digite pelo menos dois números'
            },
            'V': {
                'method': self.colorize_vertical_interval,
                'args_min': 3,
                'args_max': 4,
                'error_message': 'Digite pelo menos três números'
            },
            'H': {
                'method': self.colorize_horizontal_interval,
                'args_min': 3,
                'args_max': 4,
                'error_message': 'Digite pelo menos três números'
            },
            'K': {
                'method': self.draw_rectangle,
                'args_min': 4,
                'args_max': 5,
                'error_message': 'Digite pelo menos quatro números'
            },
            'S': {
                'method': self.save,
                'args_min': 1,
                'args_max': 1,
                'error_message': 'Digite o nome do arquivo'
            },
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
