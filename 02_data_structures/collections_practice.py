"""
Тема: Структуры данных (списки, кортежи, словари).
"""

# 1. Список кортежей с координатами
locations = []
home = (55.861792, 48.574854)
parent_home = (55.8532, 48.5267)
locations.extend([home, parent_home])
print("Координаты:", locations)

# 2. Словарь с личными данными (статический и через ввод)
about_me = {"height": 164, "weight": 59, "age": 31}
print("О себе:", about_me)

# 3. Словарь со списками внутри (любимые исполнители и треки)
favorite_music = {
    "Кравц": ["Обнуляй", "Где прошла ты?"],
    "Акмаль": ["Ты мне покажи", "Раневская"],
    "Татиттера": ["Зимнее утро"],
}

for artist, songs in favorite_music.items():
    songs_string = ", ".join(songs)
    print(f"Исполнитель {artist}, его популярные треки: {songs_string}")
