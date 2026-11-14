def main():
    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    total_revenue = sum(day['revenue'] for day in days)
    best_revenue_day = max(days, key=lambda day: day['revenue'])

    average_revenue_by_day = {
        day['day']: day['revenue'] / day['orders'] for day in days
    }

    high_return_days = [
        day['day'] for day in days if day['returns'] / day['orders'] > 0.2
    ]

    print(f'выручка за неделю: {total_revenue}')
    print('день с самой большой выручкой', best_revenue_day['day'])
    print('средняя выручка на один заказ по дням')
    for day, average_revenue in average_revenue_by_day.items():
        print(f'\t {day}: {average_revenue:.2f}')
    print(f'Дни, где возвратов больше 20% заказов {high_return_days}')


if __name__ == '__main__':
    main()
