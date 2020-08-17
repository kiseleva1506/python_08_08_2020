""" Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой. """


def user_info(**kwargs: str):
    """Функция выводит информацию о пользователе

    Именованные параметры:
    name: string - имя;
    surname: string - фамилия;
    year_of_birth: string - год рождения;
    city: string - город проживания;
    e_mail: string - e-mail;
    phone: string - телефон """

    info_structure = ('name', 'surname', 'year_of_birth', 'city', 'e_mail', 'phone')
    for itm in info_structure:
        try:
            print(kwargs[itm], end=' ')
        except KeyError:
            continue
    print()


user_info(name='Ivan', surname='Ivanov', year_of_birth='1979', city='Moscow',
          e_mail='example@google.com', phone='999-88-77')
user_info(year_of_birth='1979', city='Moscow', phone='999-88-77', name='Oleg')
