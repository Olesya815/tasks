# TODO здесь писать код

first_list = []
second_list = []

for i in range(3):
    number_the_first_list = int(input(f'Введите {i + 1}-е число для первого списка: '))
    first_list.append(number_the_first_list)
for j in range(7):
    number_the_second_list = int(input(f'Введите {j + 1}-е число для второго списка: '))
    second_list.append(number_the_second_list)

print('Первый список: ', first_list)
print('Второй список: ', second_list)

first_list.extend(second_list)

for num in first_list:
    while first_list.count(num) >= 2:
        first_list.remove(num)

print('Новый первый список с уникальными элементами: ', first_list)