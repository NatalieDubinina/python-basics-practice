"""
Тема: Бесконечный цикл while и условные операторы.
Мини-игра «Угадай число».
"""


def play_game():
    secret_numbers = ["1", "2", "3", "4", "5"]

    while True:
        guess = input("Введите число от 1 до 10 (или 'x' для выхода): ").strip()

        if guess.lower() == "x":
            print("Выход из игры. До встречи!")
            break
        elif guess in secret_numbers:
            print("Вы угадали!")
        else:
            print("Вы не угадали! Попробуйте еще раз.")


if __name__ == "__main__":
    play_game()
