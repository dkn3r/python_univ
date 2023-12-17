from task2 import Employee


class Manager(Employee):


    def __init__(self, name, salary, days, percentBonus=0,countSubordinates=0):
        super().__init__(name, salary, days, percentBonus)
        self._countSubordinates = countSubordinates
        self.premium = 2500


    def report(self):
        return f"Manager {self._name} manages: {self._countSubordinates} subordinates."

    def calculate_bonus(self):
        return super().bonus() + self._countSubordinates * self.premium
