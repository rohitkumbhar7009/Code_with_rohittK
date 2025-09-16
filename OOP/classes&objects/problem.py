class Student:
    def set_details (self,name,age):
       self.name=name
       self.age= age

student1 = Student()
student1.set_details("udit",26)

print(f'Student Name-{student1.name} Student Age -{student1.age}')