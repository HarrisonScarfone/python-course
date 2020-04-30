import names
import random

from person import Person
from class_list import Class_List
from school import School

def make_random_student():
    return Person(
        random.choice(names.last_names),
        random.choice(names.first_names),
        random.randint(6, 18),
        random.randint(1,12),
        random.randint(0, 100),
    )

def make_random_name():
    return f'{random.choice(names.first_names)} {random.choice(names.last_names)}'

def make_random_school_name():
    return  make_random_name() + ' Public School'

def make_school(lb_student, ub_student, lb_classes, ub_classes):
    school = School(make_random_school_name())
    for _ in range(random.randint(lb_classes, ub_classes)):
        class_list = Class_List(make_random_name(), [])
        for __ in range(random.randint(lb_student, ub_student)):
            class_list.add_student(make_random_student())
        school.school_classes.append(class_list)
    return school
