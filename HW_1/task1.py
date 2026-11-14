def main():
    moscow_products = {201, 202, 203, 204}
    kazan_products = {203, 204, 205, 206}

    both_cities = moscow_products & kazan_products
    only_moscow = moscow_products - kazan_products
    only_kazan = kazan_products - moscow_products
    all_products = moscow_products | kazan_products

    print(f'можно забрать в любом из двух городов {sorted(both_cities)}')
    print(f'есть только в Москве {sorted(only_moscow)}')
    print(f'есть только в Казани {sorted(only_kazan)}')
    print(f'всего разных товаров {len(all_products)}')


if __name__ == '__main__':
    main()
