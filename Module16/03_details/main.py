shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],['педаль', 100], ['седло', 1500], ['рама', 12000],
['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
detail = input('Название детали: ')
price = int(input('Введите стоимость детали'))
shop.extend([[detail, price]])
print(shop)

count = 0
summ = 0

for i in range(len(shop)):
        if detail == shop[i][0]:
                count += 1
                total_cost = shop[i][1]
                summ += total_cost
print('Количество деталей: ', count)
print('Общая стоимость: ', summ)
