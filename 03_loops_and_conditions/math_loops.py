"""
Тема: Циклы for, функция enumerate, вложенные циклы и модуль statistics.
"""
import statistics

# 1. Нумерация элементов списка
shows = ["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневники вампира"]
for index, item in enumerate(shows, start=1):
    print(index, item)

# 2. Вывод чисел в диапазоне
print("Числа от 25 до 50:", list(range(25, 51)))

# 3. Попарное перемножение элементов двух списков
list_1 = [8, 19, 148, 4]
list_2 = [9, 1, 33, 83]
multiplied = [i * j for i in list_1 for j in list_2]
print("Произведения:", multiplied)

# 4. Поиск моды (самого частого числа) в списке
numbers = [1, 5, 3, 4, 5, 6, 7, 5, 9, 10]
print("Мода списка:", statistics.multimode(numbers))
