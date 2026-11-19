"""
Задача: Планировщик рабочего дня.
Посчитать, сколько часов останется на отдых после выполнения всех задач (рабочий день — 8 часов).
"""


def calculate_free_time(tasks: list, workday_hours: float = 8.0) -> float:
    total_task_time = sum(task[1] for task in tasks)
    remaining_time = workday_hours - total_task_time
    return round(remaining_time, 1)


if __name__ == "__main__":
    todo_list = [
        ["Разобрать почту", 1],
        ["Обзвонить клиентов", 2],
        ["Запланировать дела на завтра", 0.6],
        ["Сделать презентацию", 3],
        ["Созвон с командой", 0.5],
    ]
    print("Осталось времени на отдых (ч):", calculate_free_time(todo_list))
