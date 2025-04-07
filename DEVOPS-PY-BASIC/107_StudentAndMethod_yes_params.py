# Class -> method that has parameters
class Student:
    def profile(self,name,roll):
        print("Name of the student = ",name)
        print("Roll of the student = ",roll)

stu = Student()

stu.profile("Karthik",123)  # method call
studentName = "Rahul"
studentRoll = 102
print("----------------------------------------")
print("Case 1: Method Call")
stu.profile("Karthik",123)
print("----------------------------------------")
print("Case 2: Passing parameters as Positional Arguments")
stu.profile(studentName,studentRoll)
print("----------------------------------------")
print("Case 3: Passing parameters as Keyword Arguments")
stu.profile(roll=studentRoll,name=studentName)
print("----------------------------------------")

