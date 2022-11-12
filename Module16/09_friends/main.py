# # TODO здесь писать код
number_of_friends = int(input('Количество друзей: '))
debt_receipts = int(input('Долговых расписок: '))
friends_list = []

for _ in range(number_of_friends):
    friends_list.append(0)

for i in range(debt_receipts):
    print(f'{i + 1}-я расписка: ')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[from_whom - 1] += how_much
    friends_list[to_whom - 1] -= how_much

print("Баланс друзей: ")
for index in range(len(friends_list)):
    print(index + 1, ": ", friends_list[index])