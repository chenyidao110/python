class Student:
    """student"""
    def __init__(self, name, age):
        """init method"""
        self.name = name
        self.age = age

    def study(self,course_name):
        """Studying"""
        print(f'{self.name} is studying {course_name}.')

    def play(self):
        """playing"""
        print(f'{self.name} is playing game.')

    def __repr__(self):
        return f'{self.name}: {self.age}'


stu1 = Student('luohao',40)
print(stu1)
students = [stu1,Student('wangxiaochui', 16), Student('wangdachui', 25)]
print(students)
