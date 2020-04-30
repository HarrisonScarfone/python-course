class School:

    def __init__(self, name=None, school_classes=[]):
        self.name = name
        self.school_classes = school_classes

    def how_many_school_classes(self):
        return len(self.school_classes)

    def how_many_classes(self):
        return len(self.school_classes)

    def how_many_students(self):
        student_total = 0
        for school_class in self.school_classes:
            student_total += len(school_class.student_list)
        return student_total
