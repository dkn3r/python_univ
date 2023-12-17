import re

import requests
from bs4 import BeautifulSoup


def usd_eur():
    while True:
        request = input("Введіть валюту (usd/eur): ")
        if request.lower() == "eur" or request.lower() == "usd":
            return request
        else:
            print("Error! Введіть 'usd' або 'eur'")


def currency(request):
    URL = "https://informer.com.ua/currency-rates/"
    response = requests.get(URL)
    response.raise_for_status()  # перевірка, чи відповідь успішна
    soup = BeautifulSoup(response.text, 'html.parser')
    # Знаходження всіх елементів з класом "currency-value"
    currency_data = soup.find_all("td", class_="currency-value")

    usd = currency_data[0].get_text()
    eur = currency_data[1].get_text()
    usd_value = re.findall(r'\d+\.*\d*', usd)
    eur_value = re.findall(r'\d+\.*\d*', eur)
    if request.lower() == "usd":
        return float("".join(usd_value))
    else:
        return float("".join(eur_value))


def calculation_salary(info_employers):
    result_salary = {}
    for name, data in info_employers.items():
        salary_per_month = data['salary'] / 30 * data['days']
        result_salary[name] = salary_per_month
    return result_salary


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
