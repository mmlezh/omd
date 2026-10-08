# Дана история поисковых запросов: каждая строка — один введённый запрос. Повтор в списке значит, что этот запрос ввели ещё раз.

# ```python
# queries = [
#     "чехол",
#     "iphone",
#     "чехол",
#     "наушники",
#     "iphone",
#     "iphone",
#     "кабель",
#     "чехол",
#     "iphone",
# ]
# ```

# Нужно найти:

# - сколько всего поисковых запросов в ленте
# - сколько раз ввели каждый запрос
# - какой запрос вводили чаще всего
# - какую долю всех поисков он занимает
# - какие запросы встретились один раз

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

total = len(queries)

counts = {}
for q in queries:
    counts[q] = counts.get(q, 0) + 1

most_popular = max(counts, key=counts.get)
part = counts[most_popular]/total
singles = [q for q, count in counts.items() if count == 1]

print(f'всего запросов {total}')
print(f'сколько раз ввели каждый запрос {counts}')
print(f'самый популярный запрос {most_popular}')
print(f'его доля {part:.2%}')
print(f'запросы, которые встретились один раз {singles}')
