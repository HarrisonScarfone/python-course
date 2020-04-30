class Class_List:

    def __init__(self, class_name=None, student_list=[]):
        self.class_name = class_name
        # note that passing a non-list type for students will adversly affect
        self.student_list = student_list
    
    def __repr__(self):
        return f'An object for {self.class_name} which has {len(self.student_list)} students.'

    def add_student(self, student):
        self.student_list.append(student)

    def how_many_students(self):
        return len(self.student_list)