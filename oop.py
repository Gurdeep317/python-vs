class Student:
# class attribute
    college_name="xyz"
    # default constructor
    def __init__(self):
        pass
    # parameterized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding student")
        # methods
    def welcome(self):
        print("welcome student")

s1=Student("karan",45)
(s1.welocme)
print(s1.marks,s1.name)
print(Student.college_name)
