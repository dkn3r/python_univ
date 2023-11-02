from person import Person


class IndividualStudent(Person):
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        super().__init__(name, age,prac_score, prac_count, exam_scr)



    def total_mark(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        return 0.7 * S_pr + 0.3 * S_ex

    def display_info(self):
        super().display_info()
        print("Individual student: ")