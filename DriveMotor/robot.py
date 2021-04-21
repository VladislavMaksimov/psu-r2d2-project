from threading import Timer

class Robot(object):
    """
        Задаёт действия R2-D2. Принимает поле, по которому движется робот.
        Робот начинает движение в левом верхнем углу.

        Атрибуты
        ----------
        __y : int
            координата робота по вертикали
        __x : int
            координата робота по горизонтали
        __field : list
            пространство, в котором перемещается робот
        __speed : int
            скорость робота

        Методы
        ----------
        step_right()
            робот делает один шаг вправо
        go_right()
            робот проходит вправо до препятствия
        print()
            выводит пространство с текущим положением робота в консоль
    """

    def __init__(self, field):
        self.__field = field
        self.__y = 1
        self.__x = 1
        self.__field[self.__x][self.__y] = 'x'
        self.__speed = 1
        self.print()

    def step_rigth(self):
        if self.__field[self.__y][self.__x + 1] != '-':
            self.__field[self.__y][self.__x] = '.'
            self.__x += 1
            self.__field[self.__y][self.__x] = 'x'
            self.print()
        else:
            # здесь сервис отправить сообщение AcousticSignaller, чтобы тот просигналил что-нибудь
            raise TypeError

    def go_right(self):
        try:
            self.step_rigth()
            Timer(self.__speed, self.go_right).start()
        except TypeError:
            return

    def print(self):
        for row in self.__field:
            row_str = ''
            for elem in row:
                row_str += elem
            print(row_str)