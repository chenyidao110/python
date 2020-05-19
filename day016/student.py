class Student:

    def study(self,course_name):
        print(f'students are studying {course_name}.')

    def play(self):
        print(f'students are playing.')


stu1 =  Student()
stu2 = Student()

print(stu1)
print(stu2)
print(hex(id(stu1)),hex(id(stu2)))

Student.study(stu1,'Python Programme Design')
stu1.study('Python Programe Design')

Student.play(stu2)
stu2.play()
