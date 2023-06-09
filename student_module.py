from subject_module import Subject


class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    @staticmethod
    def add_mark(mark):
        return Subject().marks.append(mark)

    @staticmethod
    def get_all_marks():
        return Subject().marks


    @staticmethod
    def calc_average():
        sum = 0
        for i in Subject().marks:
            sum += i

        conut = len(Subject().marks)
        return sum / conut