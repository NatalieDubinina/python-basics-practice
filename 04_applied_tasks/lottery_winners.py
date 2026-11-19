"""
Задача: Конкурс в магазине «Шестёрочка».
Победителем становится каждый третий покупатель.
Функция возвращает список номеров чеков победителей и их количество.
"""


def get_winners(receipts: list) -> tuple[list, int]:
    winners = []
    count = 0

    for i, number in enumerate(receipts):
        if (i + 1) % 3 == 0:
            winners.append(number)
            count += 1

    return winners, count


if __name__ == "__main__":
    sample_receipts = [123, 145, 346, 246, 235, 166, 112, 351, 436]
    winning_tickets, total_winners = get_winners(sample_receipts)
    print(winning_tickets, total_winners)
