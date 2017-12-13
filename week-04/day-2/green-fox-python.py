class Person:

    def __init__(self, name=None, age=None, gender=None):
        if name is None:
            self.name = "Jane Doe"
        else:
            self.name = name  
        
        if age is None:
            self.age = 30
        else:
            self.age = age
        
        if gender is None:
            self.gender = "female"
        else:
            self.gender = gender

    def introduce(self):
        print("Hi, I'm " + self.name + " a " + str(self.age) + " year old " + self.gender)

    def get_goal(self):
        print("My goal is: Live for the moment!")


class Student(Person):
    def __init__(self, name, age, gender, previous_organization=None, skipped_days=None): 
        super().__init__(name=None, age=None, gender=None)

        if previous_organization is None:
            self.previous_organization = "The School of Life"
        else:
            self.previous_organization = previous_organization

        if skipped_days is None:
            self.skipped_days = 0
        else:
            self.skipped_days = skipped_days

    def introduce(self):
        print("Hi, I'm " + self.name + " , " + str(self.age) + " year old " + self.gender + " from " + self.previous_organization + " who skipped " + str(self.skipped_days) + " days from the course already.")

    def get_goal(self):
        print("My goal is: Be a Junior Software Developer")
        
    def skip_days(number_of_days):
        self.skipped_days + number_of_days

class Mentor(Person):
    def __init__(self, name, age, gender, level=None): 
        super().__init__(name=None, age=None, gender=None)

        if level is None:
            self.level = "intermediate"
        else:
            self.level = level
    
    def get_goal(self):
        print("Educate brilliant software developers.")

    def introduce(self):
        print(" Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender + " " + self.level + " mentor.")

class Sponsor(Person):
    def __init__(self, name, age, gender, company, hired_students):
        super().__init__(name=None, age=None, gender=None)

    def introduce(self):
        print(" Hi, I'm " + self.name + " a " + str(self.age) + " year old " + self.gender + " who represents " + self.company + " and hired " + self.hired_students + " students so far.")

    def get_goal(self):
        print(" Hire brilliant junior software developers!")
    
    def hire(self):
        self.hired_students + 1
        



stud1 = Student()
stud1.introduce()