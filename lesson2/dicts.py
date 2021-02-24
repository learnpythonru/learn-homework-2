import collections

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# students = [
#   {'first_name': 'Вася'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Петя'},
# ]

# all_names = []
# for name in students:
#     all_names.append(name['first_name'])

# names_counter = collections.Counter(all_names)

# for name in names_counter:
#     print(f'{name}: {names_counter[name]}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
# students = [
#   {'first_name': 'Вася'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Оля'},
# ]

# all_names = []
# for name in students:
#    all_names.append(name['first_name'])

# common_name = collections.Counter(all_names).most_common(1)
# print(f'Самое частое имя среди учеников: {common_name[0][0]}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3

# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# school_students = [
#   [  # это – первый класс
#     {'first_name': 'Вася'},
#     {'first_name': 'Вася'},
#   ],
#   [  # это – второй класс
#     {'first_name': 'Маша'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Оля'},
#   ]
# ]

# def define_common_name(clas):
#     all_names = []
#     for name in clas:
#         all_names.append(name['first_name'])

#     common_name = collections.Counter(all_names).most_common(1)
#     return common_name[0][0]

# i = 1
# for clas in school_students:
#     most_common_name = define_common_name(clas)
#     print(f'Самое частое имя в классе {i}: {most_common_name}')
#     i += 1

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# school = [
#   {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#   {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
# ]
# is_male = {
#   'Маша': False,
#   'Оля': False,
#   'Олег': True,
#   'Миша': True,
# }

    

# def count_girls_in_class(clas, names_info):
#     students = clas['students']
#     girls = 0
#     for name in students:
#         student_name = name['first_name']
#         if student_name in names_info:
#             if names_info[student_name] is False:
#                 girls += 1
#     return girls

# def count_boys_in_class(clas, names_info):
#     students = clas['students']
#     boys = 0
#     for name in students:
#         student_name = name['first_name']
#         if student_name in names_info:
#             if names_info[student_name] is True:
#                 boys += 1
#     return boys

# for clas in school:
#     class_name = clas["class"]
#     girls_amount = count_girls_in_class(clas, is_male)
#     boys_amount = count_boys_in_class(clas, is_male)
#     print(f'В классе {class_name} {girls_amount} девочки и {boys_amount} мальчика.')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


def count_girls_in_class(clas, names_info):
    students = clas['students']
    girls = 0
    for name in students:
        student_name = name['first_name']
        if student_name in names_info:
            if names_info[student_name] is False:
                girls += 1
    return girls

def count_boys_in_class(clas, names_info):
    students = clas['students']
    boys = 0
    for name in students:
        student_name = name['first_name']
        if student_name in names_info:
            if names_info[student_name] is True:
                boys += 1
    return boys


class_with_most_boys = ''
for clas in school:
    class_name = clas["class"]
    boys_amount = count_boys_in_class(clas, is_male)
    max_boys_amount = 0
    if boys_amount > max_boys_amount:
        max_boys_amount = boys_amount
        class_with_most_boys = class_name

class_with_most_girls = ''
for clas in school:
    class_name = clas["class"]
    girls_amount = count_girls_in_class(clas, is_male)
    max_girls_amount = 0
    if girls_amount > max_girls_amount:
        max_girls_amount = girls_amount
        class_with_most_girls = class_name


print(f'Больше всего мальчиков в классе {class_with_most_boys}')
print(f'Больше всего девочек в классе {class_with_most_girls}')



# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a