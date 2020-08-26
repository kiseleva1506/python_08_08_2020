""" Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт. """

import time


class TrafficLight:
    """
    Класс ССветофор
    последовательность цветов: 'red', 'yellow', 'green'
    время работы: 'red': 7, 'yellow': 2, 'green': 9
    """
    __COLOR_ORDER = ('red', 'yellow', 'green')
    __COLOR_TIME = {'red': 7, 'yellow': 2, 'green': 9}

    def __init__(self):
        """
        Светофор всегда начинает работать с цвета red
        """
        self.__color = 'red'

    def get_next_color(self, current_color):
        """
        функция возвращает следующий цвет светофора
        :param current_color: str
        :return: следующий цвет: str
        """
        try:
            return self.__COLOR_ORDER[self.__COLOR_ORDER.index(current_color) + 1]
        except IndexError:
            return self.__COLOR_ORDER[0]

    def get_current_color(self):
        return self.__color

    def running(self, time_running=60, color=None):
        current_time = time.time()
        while time.time() - current_time < time_running:
            next_color = self.get_next_color(self.__color)
            if color is not None and color != next_color:
                raise ValueError('Нарушена последовательность цветов светофора!')

            self.__color = next_color
            print(f'{self.__color}: время работы {self.__COLOR_TIME[next_color]}')
            time.sleep(self.__COLOR_TIME[next_color])
            color = None


tl = TrafficLight()
tl.running(color='yellow', time_running=20)
print(tl.get_current_color())

# исключение - неправильный порядок цветов светофора
tl.running(color='white', time_running=15)
