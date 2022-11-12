# TODO здесь писать код

count = 0
number_of_skates = int(input('Введите количество коньков: '))
for i in range(number_of_skates):
    pair_size = int(input(f'Размер {i + 1}-й пары: '))

number_of_people = int(input('Количество людей: '))
for j in range(number_of_people):
    foot_size = int(input(f'Размер ноги {j + 1}-го человека: '))
    if foot_size == pair_size or pair_size > foot_size:
        count += 1
print('Наибольшее кол-во людей, которые могут взять ролики: ', count)