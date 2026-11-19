"""
Задача: Гонка зайца и черепахи.
Подсчитать пройденную дистанцию по шагам и определить победителя.
"""


def get_race_winner(hare_steps: list, turtle_steps: list) -> str:
    hare_total = 0
    turtle_total = 0

    for i in range(len(hare_steps)):
        hare_total += hare_steps[i]
        turtle_total += turtle_steps[i]

    if hare_total == turtle_total:
        return "одинаково"
    elif hare_total > turtle_total:
        return "заяц"
    else:
        return "черепаха"


if __name__ == "__main__":
    hare_distance = [8, 5, 3, 2, 0, 1, 1]
    turtle_distance = [3, 3, 3, 2, 0, 1, 1]
    print("Победитель:", get_race_winner(hare_distance, turtle_distance))
