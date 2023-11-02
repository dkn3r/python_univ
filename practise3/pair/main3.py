def input_product():
    products = {}

    while True:
        name = input("Введ. назву або 'stop' щоб закінчити:")

        if name.lower() == 'stop':
            break

        price = float(input("Введіть ціну товару:"))
        stock = int(input("Введіть залишок товару на складі:"))
        products[name] = {'Ціна': price, 'Залишок': stock}

    return products


def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details["Ціна"] * details["Залишок"]
        print(f"Вартість залишку для {product}: {stock_value}")
