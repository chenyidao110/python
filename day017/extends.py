class Person:
    """Person class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating.')

    def sleep(self):
        print(f'{self.name} is sleeping.')



class Student(Person):
    """student class"""

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name} is studying {course_name}.')


class Teacher(Person):
    """Teacher class"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self,course_name):
        print(f'{self.name} {self.title} is teaching {course_name}')

