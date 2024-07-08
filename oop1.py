class Student:
    def __init__(self,firstname,age,course,gender):
        self.firstname = firstname
        self.age = age
        self.course = course
        self.gender = gender

    def study(self):
        print(self.firstname,"is studying")
student1 = Student("Job",21,"MIT","Male")
student1.study()
print(student1.gender)
student2 = Student("Ann",13,"Datascience","Female")
student2.study()
student3 = Student("Joe",34,"Cybersecurity","Male")


