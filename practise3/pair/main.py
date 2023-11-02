from main2 import create_matrix, print_products
from main3 import input_product, calculate_stock_value

products = input_product()
print(products)

calculate_stock_value(products)

product_matrix = create_matrix(products)
print_products(product_matrix)
