from datetime import date


class Student:

    def __init__(self, stuID, n, DOB, c):
        self.__studentID = stuID
        self.__name = n
        self.__DOB = DOB
        self.__classification = c
        self.__age = 0
        self.__register = ''

    def student_age(self):
        today = date.today()
        year = today.year
        age = self.__DOB.split('/')  # splits where theres a /
        birth_year = int(age[2])
        self.__age = year - birth_year

    def register_date(self):
        if self.__classification == 'senior':
            self.__register = '4/1 thru 4/3'
        elif self.__classification == 'junior':
            self.__register = '4/4 thru 4/6'
        elif self.__classification == 'sophomore':
            self.__register = '4/7 thru 4/9'
        elif self.__classification == 'freshman':
            self.__register = '4/10 thru 4/12'
        else:
            self.__register = 'classification not found'

    def get_age(self):
        return self.__age

    def get_rdate(self):
        return self.__register
