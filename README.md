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
