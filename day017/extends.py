class Person:
    """person class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is slepping.')


class Student(Person):
    """student class"""

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name} is studying {course_name}.')


class Teacher(Person):
    """teacher class"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name} {self.title} is teaching {course_name}')

stu1 = Student('baiyuanfang', 21)
stu2 = Student('direnjie', 22)
teacher = Teacher('wuzetian', 35, 'fujiaoshou')

stu1.eat()
stu2.sleep()

teacher.teach('Python Programme Design')
stu1.study('Python Programme Design')
