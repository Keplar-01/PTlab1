# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType, StudentType
from src.StudentsHelper import StudentsHelper


class TestStudentsHelper:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, StudentType]:
        data: DataType = {
            "Иванов Константин": [
                ("математика", 80), ("физика", 85), ("химия", 78)
            ],
            "Петров Петр": [
                ("математика", 70), ("физика", 60), ("химия", 75)
            ],
            "Сидоров Сидор": [
                ("математика", 76), ("физика", 76), ("химия", 76), ("литература", 80)
            ],
            "Кузнецов Алексей": [
                ("математика", 90), ("физика", 82), ("химия", 90)
            ]
        }
        student: StudentType = [
            "Иванов Константин",
            "Сидоров Сидор",
            "Кузнецов Алексей",
        ]

        return data, student

    def test_init_students_helper(self,
                                  input_data: tuple[DataType, StudentType]) -> None:
        helper = StudentsHelper(input_data[0])

        assert input_data[0] == helper.data

    def get_student_by_rating_upper_76(self, input_data: tuple[DataType, StudentType]) -> None:
        helper = StudentsHelper(input_data[0])

        expected = input_data[1]
        result = helper.get_student_by_rating_upper_76()


        assert set(result) == set(expected)