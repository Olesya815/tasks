# TODO здесь писать код
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')

while True:
    question = input('Гость пришел или ушел? ')
    if question == 'пришел' or question == 'Пришел':
        guest_name = input('Имя гостя: ')
        if len(guests) >= 6:
            print(f'Прости, {guest_name}, но мест нет')
        else:
            guests.append(guest_name)
            print(f'Привет, {guest_name}')
        print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    elif question == 'ушел' or question == 'Ушел':
        guest_name = input('Введите имя гостя: ')
        guests.remove(guest_name)
        print(f'Пока, {guest_name}')
        print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    elif question == 'пора спать' or question == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break


