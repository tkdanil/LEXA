import random
from datetime import timedelta
from typing import Iterable, Any
def get_duration(playlist: Iterable, n: int) -> Any:   
    if isinstance(playlist, list) and len(playlist) == 2:
        # Если плейлист - это список из кортежей
        songs, durations = playlist
        song_duration_dict = dict(zip(songs, durations))
    elif isinstance(playlist, dict):
        # Если плейлист - это словарь
        song_duration_dict = playlist
    else:
        raise ValueError("Invalid playlist format")
    n = min(n, len(song_duration_dict))
    selected_songs = random.sample(list(song_duration_dict.items()), n)
    total_duration = sum(duration for song, duration in selected_songs)
    return timedelta(hours=int(total_duration // 60), minutes=int(total_duration % 60))
# Пример использования
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

# Запрос на 3 случайные песни из первого плейлиста
print(get_duration(playlist_d, 3))

# Запрос на 5 случайных песен из второго плейлиста
print(get_duration(playlist_b, 5))
