""" Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных. """


class Date:
    date_str = ""

    def __init__(self, date_str):
        Date.date_str = date_str

    def __str__(self):
        return self.date_str

    @classmethod
    def extract_data(cls):
        return map(int, cls.date_str.split('-'))

    @staticmethod
    def validate_data(day, month, year):
        if day < 1 or day > 31:
            print('С днем точно что-то не в порядке')
        elif 28 < day < 32:
            print('В некотором месяце вам точно повезет с таким числом')
        else:
            print('Этот день хорош для любого месяца любого года, даже високосного')

        if month < 1 or month > 12:
            print('С месяцем точно промахнулись')

        if year < 1:
            print('Промахнуться с годом было сложно, но у вас получилось')


if __name__ == '__main__':
    some_date = Date('13-22-0000')
    d, m, y = Date.extract_data()
    Date.validate_data(d, m, y)
