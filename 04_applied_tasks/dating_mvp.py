"""
Задача: MVP dating-сервиса.
Отсортировать списки парней и девушек по алфавиту и составить пары по одинаковым индексам.
"""


def match_couples(boys: list, girls: list) -> str:
    if len(boys) != len(girls):
        return "Кто-то может остаться без пары!"

    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)

    pairs = [f"{boy} и {girl}" for boy, girl in zip(sorted_boys, sorted_girls)]
    return ", ".join(pairs)


if __name__ == "__main__":
    boys_list = ["Peter", "Alex", "John", "Arthur", "Richard"]
    girls_list = ["Kate", "Liza", "Kira", "Emma", "Trisha"]
    print(match_couples(boys_list, girls_list))
