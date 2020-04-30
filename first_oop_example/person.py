class Person:
    def __init__(self, first_name, last_name, age, grade, average):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        self.average = average

    def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(
            self.last_name,
            self.first_name, 
            self.age, 
            self.grade, 
            self.average
        )

    def change_grade(self, new_grade):
        if self.grade > 0 and self.grade < 13:
            self.grade  = new_grade

    def change_average(self, new_average):
        self.average = new_average
