"""
Задача: Поиск палиндромов.
Вывести списком все фразы, которые одинаково читаются в обоих направлениях (без учёта пробелов).
"""


def find_palindromes(phrases_list: list) -> list:
    palindromes = []
    for phrase in phrases_list:
        cleaned = phrase.replace(" ", "").lower()
        if cleaned == cleaned[::-1]:
            palindromes.append(phrase)
    return palindromes


if __name__ == "__main__":
    phrases = [
        "нажал кабан на баклажан",
        "дом как комод",
        "рвал дед лавр",
        "азот калий и лактоза",
        "а собака боса",
        "тонет енот",
        "карман мрак",
        "пуст суп",
    ]
    print(find_palindromes(phrases))
