class Student:
    """student"""

    def __init__(self, name, age):
        """init method"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """Studying"""
        print(f'{self.name} is studying {course_name}.')

    def play(self):
        """playing"""
        print(f'{self.name} is playing games.')


stu1 = Student('luohao',40)
stu2 = Student('wangdachui',15)
stu1.study('Python Programme Design')
stu2.play()
