class Person():
    def __init__(self,name="Jane Doe",age=30,gender="female"):
        self.name = name
        self.age = age
        self.gender = gender
        self.goal = "Live for the moment!"
    
    def introduce(self):
        print("Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + ".")

    def get_goal(self):
        print("My goal is: " + self.goal)

class Student(Person):
    def __init__(self,previous_organization="School of Life",skipped_days=0):
        super().__init__(name="Jane Doe",age=30,gender="female")




person1 = Person()
person1.introduce()
person1.get_goal()

student1 = Student()
student1.introduce()