def main():
    reviews = [
        {'id': 1, 'product': 'Чехол', 'stars': 5},
        {'id': 1, 'product': 'Чехол', 'stars': 3},
        {'id': 1, 'product': 'Чехол', 'stars': 4},
        {'id': 2, 'product': 'Наушники', 'stars': 2},
        {'id': 2, 'product': 'наушники', 'stars': 2},
        {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
        {'id': 3, 'product': 'Планшет', 'stars': 5},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 5, 'product': 'Кабель', 'stars': 1},
    ]

    products = {}

    for review in reviews:
        product_name = review['product'].lower()

        if product_name not in products:
            products[product_name] = {'stars_sum': 0, 'reviews_count': 0}

        products[product_name]['stars_sum'] += review['stars']
        products[product_name]['reviews_count'] += 1

    average_ratings = {
        product_name: (
            rating_stats['stars_sum'] / rating_stats['reviews_count']
        )
        for product_name, rating_stats in products.items()
    }

    products_with_multiple_reviews = [
        product_name
        for product_name, rating_stats in products.items()
        if rating_stats['reviews_count'] >= 2
    ]

    worst_product = min(
        products_with_multiple_reviews,
        key=lambda product_name: average_ratings[product_name],
    )

    low_rating_count = sum(1 for review in reviews if review['stars'] <= 2)
    low_rating_part = low_rating_count / len(reviews)

    print('средние оценки товаров')
    for product_name, average_rating in average_ratings.items():
        print(f'\t  {product_name.capitalize()}: {average_rating:.2f}')
    print(f'худший товар, который заказали больше одного раза {worst_product}')
    print(f'Количество отзывов на 1 или 2 звезды {low_rating_count}')
    print(f'Их доля от всех отзывов: {low_rating_part:.2%}')


if __name__ == '__main__':
    main()
