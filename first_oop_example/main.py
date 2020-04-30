import make_random_stuff

school = make_random_stuff.make_school(2, 3, 1, 3)

print(f'This is {school.name}!')

print(f'These are the teachers and the students in their class!\n\n')

for school_class in school.school_classes:
    print(f'The class of {school_class.class_name} has {len(school_class.student_list)} students.')
    print('Their records are:')
    for student in school_class.student_list:
        print(f'\t{student}')


    