class Field(object):
    """
        Генерирует поле для робота.

        Атрибуты
        ----------
        field  : list
            пространство, в котором будет двигаться робот
        __height : int
            высота поля
        __width: int
            ширина поля

        Методы
        ----------
        __initialize()
            генерирует пространство
        __fill_row()
            генерирует горизонтальную линию в пространстве
        print()
            выводит пространство в консоль
    """

    def __init__(self, height, width):
        self.field = []
        self.__height = height
        self.__width = width
        self.__initialize()

    def __fill_row(self) -> list:
        row = []
        row.extend(['-'] + ['.' for j in range(self.__width - 2)] + ['-'])
        return row

    def __initialize(self) -> list:
        field = []
        for i in range(self.__height):
            row = []
            if i == 0 or i == self.__height - 1:
                row.extend(['-' for j in range(self.__width)])
            else:
                row.extend(self.__fill_row())
            field.append(row)
        self.field = field

    def print(self):
        for i in range(self.__height):
            row = ''
            for j in range(self.__width):
                row += self.field[i][j]
            print(row)