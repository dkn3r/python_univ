class Employee():
    def __init__(self, name, salary, days, percentBonus=0):
        self._name = name
        self._salary = salary
        self._days = days
        self._percentBonus = percentBonus

    def salary_per_month(self):
        return self._salary / 30 * self._days

    def bonus(self):
        return self._salary / 100 * self._percentBonus

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def get_days(self):
        return self._days

    def set_days(self, days):
        self._days = days

    def get_bonus_percent(self):
        return self._percentBonus

    def set_percent_bonus(self, percentBonus):
        self._percentBonus = percentBonus
