# TODO здесь писать код
one_class = []
second_class = []

for index_one in range(160, 178, 2):
    one_class.append(index_one)
for index_second in range(162, 183, 3):
    second_class.append(index_second)

one_class.extend(second_class)

for external in range(len(one_class)):
    for interior in range(external, len(one_class)):
        if one_class[external] > one_class[interior]:
            one_class[external], one_class[interior] = one_class[interior], one_class[external]
print(one_class)
