# -*- coding: utf-8 -*-
import argparse
import sys
from YAMLDataReader import YAMLDataReader
from StudentsHelper import StudentsHelper


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    reader = YAMLDataReader()
    students = reader.read(path)
    print("Students: ", students)
    name_students = StudentsHelper(students).get_student_by_rating_upper_76()
    for name in name_students:
        print(name)


if __name__ == "__main__":
    main()
