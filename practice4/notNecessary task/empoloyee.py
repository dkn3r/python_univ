class Employee():
    def __init__(self, name, salary, days, percentBonus, adress):
        self._name = name
        self._salary = salary
        self._days = days
        self._percentBonus = percentBonus
        self.adress = adress

    def salary_per_month(self):
        return self.get_salary() / 30 * self.get_days()

    def bonus(self):
        return self.get_salary() / 100 * self.get_bonus_percent()

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Error! Name must be a string!")
            return -1

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if salary < 0:
            print("Error! Salary can't be negative!")
            return -1
        self._salary = salary

    def get_days(self):
        return self._days

    def set_days(self, days):
        if days < 0:
            print("Error! Days can't be negative!")
            return -1
        self._days = days

    def get_bonus_percent(self):
        return self._percentBonus

    def set_bonus_percent(self, percentBonus):
        if percentBonus < 0:
            print("Error! Bonus percent can't be negative!")
            return -1
        self._percentBonus = percentBonus

    def addresses_employee(self):
        return f"{self.get_name()} address: {self.adress.country}, {self.adress.city}, {self.adress.street} {self.adress.nbuild}"

    def info_abt_employee(self):
        return f"worked days: {self.get_days()}, salary: {self.salary_per_month()}, bonus: {self.bonus()}"
