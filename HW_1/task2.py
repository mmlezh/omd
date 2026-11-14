def main():
    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone',
    ]
    total_queries = len(queries)
    query_counts = {}
    for query in queries:
        query_counts[query] = query_counts.get(query, 0) + 1

    most_popular_query = max(query_counts, key=query_counts.get)
    most_popular_part = query_counts[most_popular_query] / total_queries
    single_occurrence_queries = [
        query
        for query, query_count in query_counts.items()
        if query_count == 1
    ]

    print(f'всего запросов {total_queries}')
    print(f'сколько раз ввели каждый запрос {query_counts}')
    print(f'самый популярный запрос {most_popular_query}')
    print(f'его доля {most_popular_part:.2%}')
    print('запросы, которые встретились один раз', single_occurrence_queries)


if __name__ == '__main__':
    main()
