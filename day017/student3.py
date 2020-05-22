class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('wangdachui', 20)
stu.sex = 'man'

print(f'{stu.name}, {stu.age}, {stu.sex}')
