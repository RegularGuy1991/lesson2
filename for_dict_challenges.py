# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from collections import Counter
print('Задание 1------------------------')

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_list = []

for dict in students:
    for name in dict:
        name_list.append(dict[name])

counter = Counter(name_list)

for i in counter:
    print(f'{i}: {counter[i]}')


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
    
print('Задание 2------------------------')    
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name_list = []

for dict in students:
    for name in dict:
        name_list.append(dict[name])

counter = Counter(name_list)

common_value = counter.most_common(1)

print(f'Самое частое имя среди учеников: {common_value[0][0]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print('Задание 3------------------------')

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


def common_name(list):
    sum_of_names = []
    for dict in list:
        sum_of_names.append(dict['first_name'])
        count = Counter(sum_of_names)
        most_common_name = count.most_common(1)
    return most_common_name[0][0]

class_num = 1

for dict in school_students:
    print(f'Самое частое имя в классе {class_num}: {common_name(dict)}')
    class_num += 1
    

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

print('Задание 4------------------------')

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def class_names(one_class, gender_list):
    names_in_class = []
    for students in one_class['students']:
        names_in_class.append(students['first_name'])
    male_in_class = 0
    female_in_class = 0
    for name in names_in_class:
        if gender_list[name] == True:
            male_in_class += 1
        else:
            female_in_class += 1
    return male_in_class, female_in_class


for class_number in school:
    gender = class_names(class_number, is_male)
    print(f"Класс {class_number['class']}: Девочки: {gender[1]} Мальчики: {gender[0]}")



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print('Задание 5------------------------')


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

for class_number in school:
    gender = class_names(class_number, is_male)
    if gender[1] > gender[0]:
        print(f"Больше всего девочек в классе: {class_number['class']}")
    else:
        print(f"Больше всего маьчиков в классе: {class_number['class']}")