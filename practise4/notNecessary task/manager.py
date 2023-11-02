from empoloyee import Employee


class Manager(Employee):
    premium = 2500

    def __init__(self, name, salary, countSubordinates, days, percentBonus, adress):
        super().__init__(name, salary, days, percentBonus, adress)
        self._countSubordinates = countSubordinates

    def calculate_bonus(self):
        bonus = super().bonus()
        return bonus + self._countSubordinates + Manager.premium

    def report(self):
        return f"Manages: {self._countSubordinates} subordinates."
