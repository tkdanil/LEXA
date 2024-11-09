playlist_d = [
("The Flute Tune", "Voodoo People", "Galvanize", "Miami Disco", "Komarovo", "Wild Frontier", "Check It Out", "Seasons", "These Things Will Come To Be"),
(5.23, 5.07, 7.34, 4.31, 2.26, 4.28, 2.09, 4.25, 4.56),
]

playlist_b = {
'Портофино': 3.32,
'Снег': 4.35,
'Попытка №5': 3.23,
'Тополиный Пух': 3.53,
'Если хочешь остаться': 4.48,
'Зеленоглазое такси': 5.52,
'Ты не верь слезам': 3.1,
'Nowhere to Run': 2.58,
'Салют, Вера': 4.44,
'Улетаю': 3.24,
'Опять метель': 3.37,
}

#решение
from random import sample
def playingtime(playlist, n):
    time = 0
    if type(playlist) == dict:
        names = sample(list(playlist.keys()), n)
        for i in names:
            time += playlist[i]
    elif type(playlist) == list and len(playlist) == 2 and type(playlist[0]) == type(playlist[1]) == tuple:
        playlist_dict = dict()
        for i in range(len(playlist[0])):
            playlist_dict[playlist[0][i]] = playlist[1][i]
        names = sample(list(playlist_dict.keys()), n)
        for i in names:
            time += playlist_dict[i]
    return time
print(playingtime(playlist_b, 3))
print(playingtime(playlist_d, 3))
