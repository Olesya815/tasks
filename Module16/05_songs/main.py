violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код

number_of_songs = int(input('Сколько песен выбрать? '))
summ = 0
for i in range(number_of_songs):
    name_of_the_song = input(f'Название {i + 1}-й песни: ')
    for j in range(len(violator_songs)):
        if name_of_the_song == violator_songs[j][0]:
            summ += violator_songs[j][1]
print('Общее время звучания песен:', round(summ, 2), 'минуты')