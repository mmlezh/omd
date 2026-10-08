# Есть список отзывов на товары. На каждой строке — по одному. Данные слегка битые, и названия товара записаны в разном регистре. `id` при этом один и тот же для одного и того же товара. Перед подсчётом приведите названия к одному формату, иначе они будут считаться как разные`.

# ```python
# reviews = [
#     {"id": 1, "product": "Чехол", "stars": 5},
#     {"id": 1, "product": "Чехол", "stars": 3},
#     {"id": 1, "product": "Чехол", "stars": 4},
#     {"id": 2, "product": "Наушники", "stars": 2},
#     {"id": 2, "product": "наушники", "stars": 2},
#     {"id": 2, "product": "НАУШНИКИ", "stars": 5},
#     {"id": 3, "product": "Планшет", "stars": 5},
#     {"id": 4, "product": "Колонка", "stars": 4},
#     {"id": 4, "product": "Колонка", "stars": 4},
#     {"id": 5, "product": "Кабель", "stars": 1},
# ]
# ```

# Нужно найти:

# - среднюю оценку каждого товара
# - худший товар по средней оценке среди тех, у кого хотя бы два отзыва
# - сколько отзывов на 1 или 2 звезды
# - какую долю всех отзывов они составляют

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

products = {}

for review in reviews:
    product = review["product"].lower()

    if product not in products:
        products[product] = {"stars_sum": 0, "reviews_count": 0}

    products[product]["stars_sum"] += review["stars"]
    products[product]["reviews_count"] += 1

average_ratings = {product: stats["stars_sum"] / stats["reviews_count"] for product, stats in products.items()}

multiple_reviews = [product for product, stats in products.items() if stats["reviews_count"] >= 2]

worst_product = min(multiple_reviews, key=lambda product: average_ratings[product])

count = sum(1 for review in reviews if review["stars"] <= 2)
part = count / len(reviews)

print("cредние оценки товаров")
for product, average_rating in average_ratings.items():
    print(f'\t  {product.capitalize()}: {average_rating:.2f}')
print(f'худший товар, который заказали больше одного раза {worst_product}')
print(f'Количество отзывов на 1 или 2 звезды {count}', count)
print(f"Их доля от всех отзывов: {part:.2%}")
