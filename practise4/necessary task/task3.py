from task2 import Employee


class Manager(Employee):
    premium = 2500

    def __init__(self, name, salary, countSubordinates, days, percentBonus):
        super().__init__(name, salary, days, percentBonus)
        self._countSubordinates = countSubordinates


    def report(self):
        return f"Manager {self._name} manages: {self._countSubordinates} subordinates."
