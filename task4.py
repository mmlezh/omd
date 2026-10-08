# Есть статистика за пять дней работы магазина. У каждого дня число заказов, выручка и число возвратов.

# ```python
# days = [
#     {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
#     {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
#     {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
#     {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
#     {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
# ]
# ```

# Нужно найти:

# - выручку за всю неделю
# - день с самой большой выручкой
# - среднюю выручку на один заказ в каждый день
# - дни, где возвратов больше 20% заказов

days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

revenue = sum(day["revenue"] for day in days)
best = max(days, key=lambda day: day["revenue"])

average_revenue = {day["day"]: day["revenue"] / day["orders"] for day in days}

bad_days = [day["day"] for day in days if day["returns"] / day["orders"] > 0.2]

print(f'выручка за неделю: {revenue}')
print(f'день с самой большой выручкой {best["day"]}')
print(f'cредняя выручка на один заказ по дням')
for day, rev in average_revenue.items():
    print(f'\t {day}: {rev:.2f}')
print(f'Дни, где возвратов больше 20% заказов {bad_days}')
