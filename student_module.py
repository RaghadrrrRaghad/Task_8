from subject_module import Subject
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def add_mark (self, mark):
        Subject().marks.append(mark)




