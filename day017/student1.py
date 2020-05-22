class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name} is studying {course_name}.')

stu = Student('wangdachui', 20)
stu.study('Python Programme Design')
print(stu._Student__name, stu._Student__age)