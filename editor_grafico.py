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


def main():
    pass


if __name__ == '__main__':
    main()
