# TODO здесь писать код

number_of_persons = int(input('Количество человек: '))
number_in_the_counter = int(input('Какое число в считалке: '))
print(f'Значит, выбывает каждый {number_in_the_counter}-й человек')
lst = []
ind = 0

for i in range(1, number_of_persons + 1):
    lst.append(i)


while len(lst) != 1:
    print(f'Текущий круг людей: {lst}')
    for _ in range(number_in_the_counter):# делаем к-раз
        if ind == len(lst):
            ind = 0
        ind += 1 # в конце цикла count=number_in_the_counter(7=7)
    ind -= 1
    print(f'Выбывает человек под номером {lst[ind]}')
    del lst[ind]
print(f'Остался человек под номером {lst}')
