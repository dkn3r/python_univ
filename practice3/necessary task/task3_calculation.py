def matrix_employers(info_employers):
    matrix_name = []
    for name, data in info_employers.items():
        matrix_name.append([name, data['salary'], data['days']])
    return matrix_name


def output_employers(matrix_employers_data, i=0):
    if i == len(matrix_employers_data):
        return
    print(f"Робочий {i + 1}: {matrix_employers_data[i][0]}")
    output_employers(matrix_employers_data, i + 1)