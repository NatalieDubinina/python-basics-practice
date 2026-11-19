"""
Задача: Калькулятор списка покупок.
Рассчитать количество ингредиентов для приготовления блюд на заданное число персон.
"""


def generate_shopping_list(recipes: list, person_count: int) -> list:
    result = []

    for dish_name, ingredients in recipes:
        formatted_ingredients = []
        for name, amount, unit in ingredients:
            total_amount = amount * person_count
            formatted_ingredients.append(f"{name} {total_amount} {unit}")

        dish_line = f"{dish_name}: {', '.join(formatted_ingredients)}"
        result.append(dish_line)

    return result


if __name__ == "__main__":
    cook_book = [
        [
            "Салат",
            [
                ["картофель", 100, "гр."],
                ["морковь", 50, "гр."],
                ["огурцы", 50, "гр."],
                ["горошек", 30, "гр."],
                ["майонез", 70, "мл."],
            ],
        ],
        [
            "Пицца",
            [
                ["сыр", 50, "гр."],
                ["томаты", 50, "гр."],
                ["тесто", 100, "гр."],
                ["бекон", 30, "гр."],
                ["колбаса", 30, "гр."],
                ["грибы", 20, "гр."],
            ],
        ],
        [
            "Фруктовый десерт",
            [
                ["хурма", 60, "гр."],
                ["киви", 60, "гр."],
                ["творог", 60, "гр."],
                ["сахар", 10, "гр."],
                ["мед", 50, "мл."],
            ],
        ],
    ]

    shopping_list = generate_shopping_list(cook_book, person_count=5)
    print(shopping_list)
