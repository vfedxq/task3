# class Parrot:
#
#     species = 'bird'
#
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
#
#
# blu = Parrot('Blu', 10)
# woo = Parrot('woo', 5)
class Student:

    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.5
        self.gladness -= 2

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 5

    def to_chill(self):
        print('Time to rest')
        self.progress -= 7
        self.gladness += 0.2


    def is_alive(self):
        if self.progress < -0.5
            self.alive = False

        elif self.gladness <= 0:
            print('Depression')
            self.alive + False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {self.progress}')