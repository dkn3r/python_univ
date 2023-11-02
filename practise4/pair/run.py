from studentFullTime import FullTimeStudent
from IndividualStudent import IndividualStudent

student1 = FullTimeStudent("Gena", 24, 910, 10, 95, 85)
student2 = IndividualStudent("Grysha", 19, 950, 10, 98)

univ_students = [student1, student2]

# print(f"Full time student: ")
# print(f"Name: {student1.name}")
# print(f"Age: {student1.age}")
# print(f"Average mark on practice: {student1.avg_practice_score()}")
# print(f"Total mark: {student1.total_mark()}\n")
#
# print(f"Individual student: ")
# print(f"Name: {student2.name}")
# print(f"Age: {student2.age}")
# print(f"Average mark on practice: {student2.avg_practice_score()}")
# print(f"Total mark: {student2.total_mark()}")

for student in univ_students:
    student.display_info()
    if isinstance(student, FullTimeStudent):
        print(f"Total mark: {student.total_mark()}")
    elif isinstance(student, IndividualStudent):
        print(f"Total mark: {student.total_mark()}")
