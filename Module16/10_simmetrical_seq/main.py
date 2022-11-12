# TODO здесь писать код
amount_of_numbers = int(input('Количество чисел: '))
lst = []
for i in range(1, amount_of_numbers + 1):
    number = int(input('Число: '))
    lst.append(i)

print('Последовательность:', lst)

for i in range(len(lst)):
    if lst[i:] == lst[i:][::-1]:
        print('Нужно приписать чисел', i)
        print(*lst[:i][::-1])
        break
