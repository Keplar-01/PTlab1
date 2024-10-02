from Types import DataType, RatingType, StudentType


class StudentsHelper:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def get_student_by_rating_upper_76(self) -> StudentType:
        students = StudentType()

        for student in self.data:
            cnt_good_subjects = 0

            for subject in self.data[student]:
                if subject[1] >= 76:
                    cnt_good_subjects += 1

            if cnt_good_subjects >= 3:
                students.append(student)

        if len(students) == 0:
            students.append("Нет студентов, у которых 3 "
                            "и более оценки выше 76")

        return students
