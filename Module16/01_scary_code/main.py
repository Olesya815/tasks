a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
t = 0
for i in a:
    if i == 5:
        t += 1
print(t)
d = []
for i in a:
    if i != 5:
        d.append(i)
for i in c:
    d.append(i)
t = 0
for i in d:
    if i == 3:
        t += 1
print(t)
print(d)

# TODO переписать программу

main = [1, 5, 3]
first_list = [1, 5, 1, 5]
second_list = [1, 3, 1, 5, 3, 3]

main.extend(first_list)
print('Количество цифр 5 при первом объеденении: ', main.count(5))

for index in main:
    if index == 5:
        main.remove(index)

main.extend(second_list)
print('Количество цифр 3 при втором объеденении: ', main.count(3))
print('Итоговый список: ', main)