class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name or 'no name'

    @property
    def age(self):
        return self.__age

stu = Student('wangdachui', 20)
print(stu.name, stu.age)
stu.name = ''
print(stu.name)
