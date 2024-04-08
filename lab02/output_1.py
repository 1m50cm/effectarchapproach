import numpy as np


class ScoreList:
    def __init__(self, *args):
        self.score_list = [i for i in args]

    def total_score(self):
        return np.sum(self.score_list)


class Person:
    def __init__(self, name, age, gender, height, weight):
        self.score_list = None
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def set_score_list(self, *args):
        self.score_list = ScoreList(args)

    def is_adult(self):
        return self.age >= 18

    def print_info(self):
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Total Score:", self.score_list.total_score())
        print("Adult:", self.is_adult())


def main():
    my_person = Person("Emy", 20, "Female", 155, 40)
    my_person.set_score_list(55, 70, 60, 81, 49)
    my_person.print_info()


if __name__ == '__main__':
    main()
