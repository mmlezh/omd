# Есть список заказов:
# - `status` -  статус заказа
#   - `delivered` доставлен покупателю
#   - `returned` возврат
# - `amount` — сумма заказа.

# ```python
# orders = [
#     {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
#     {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
#     {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
#     {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
#     {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
#     {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
# ]
# ```

# Нужно найти:

# - на какую сумму оформили возвраты
# - кто хотя бы раз вернул заказ
# - сколько заказов доставлено покупателю
# - средний чек доставленных заказов

orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

returned = [order for order in orders if order["status"] == "returned"]
delivered = [order for order in orders if order["status"] == "delivered"]

returned_amount = sum(order["amount"] for order in returned)
delivered_amount = sum(order["amount"] for order in delivered)
buyers = {order["buyer"] for order in returned}
delivered_count = len(delivered)
average = delivered_amount / delivered_count

print(f'сумма возвратов {returned_amount}')
print(f'покупатели, вернувшие заказы {sorted(buyers)}')
print(f'количество доставленных заказов {delivered_count}')
print(f'средний чек доставленных заказов {average:.2f}')
