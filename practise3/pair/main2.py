def create_matrix(product_info):
    matrix = []
    for product, details in product_info.items():
        matrix.append([product, details["Ціна"], details["Залишок"]])
    return matrix


def print_products(matrix, index=0):
    if index == len(matrix):
        return
    print(matrix[index][0])
    print_products(matrix, index + 1)
