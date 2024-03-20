import pytest

import pandas as pd
from student_supervisor.allocate import allocate_students
from importlib.resources import files
import tests.testdata


def test_can_allocate_students_to_supervisors():
    students = pd.read_csv(
        files(tests.testdata).joinpath("student_preference.csv")
    )
    student_names = students["name"].values
    supervisor_capacity = pd.read_csv(
        files(tests.testdata).joinpath("supervisor_capacity.csv")
    )
    allocated = allocate_students(students, supervisor_capacity)

    for supervisor, student in allocated.items():
        print(
            f"{supervisor} ({len(student)} / {supervisor.capacity}): {student}")

    matched_students = []
    for _, students in allocated.items():
        for student in students:
            matched_students.append(student.name)

    unmatched_students = set(student_names).difference(
        matched_students
    )
    assert len(unmatched_students) == 0
