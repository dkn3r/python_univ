products = {}


def add_product(products, name, price, quantity, sale):
    if name in products:
        products[name]['quantity'] += quantity
        products[name]['sale'] = sale
    else:
        products[name] = {'price': price, 'quantity': quantity, 'sale': sale}


def sell_product(products, name, quantity):
    if name in products and products[name]['quantity'] >= quantity:
        # Вирахування знижки
        discount_price = product_with_sale(products,name)
        products[name]['quantity'] -= quantity
        return discount_price * quantity
    else:
        print(f"Товару {name} недостатньо на складі або його немає!")
        return 0
def product_with_sale(products,name):
    product_price = products[name]['price']
    product_sale = products[name]['sale']
    price_result = product_price - (product_price * product_sale / 100)
    return price_result

# Виведення всього наявного товару
def show_products():
    print('\nТовару на складі:')
    for name, data in products.items():
        print(f'{name}: Ціна: {product_with_sale(products,name)} | Кількість: {data["quantity"]} | Знижка: {data["sale"]}% | ')

# Додаємо продукти
add_product(products, "apple", 10, 10, 5)
add_product(products, "banana", 5, 15, 15)
add_product(products, "cherry", 20, 5, 7)




show_products()
# Продаємо декілька продуктів з врахуваннням знижки
print('\n')
profit = 0
profit += sell_product(products, "apple", 5)
profit += sell_product(products, "cherry", 3)
profit += sell_product(products, "grape", 2)  # Цей продукт не існує на складі, тому виведеться повідомлення

print(f"\nЗагальний прибуток: {profit} грн.")
