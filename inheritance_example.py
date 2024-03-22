class Identity:
    def __init__(self,name,age,gender):
        self._name=name
        self._age=age
        self._gender=gender

    def get_details(self):
        self.name=input("Enter the name: ")
        self.age=int(input("Enter the age: "))
        self.gender=input("Enter the gender: ")
class Teacher(Identity):
    def __init__(self,name,age,gender,exp,subject):
        super().__init__(name,age,gender)
        self.exp=exp
        self.subject=subject

    def get_details(self):
        super().get_details()
        self.subject=input("Enter the subject: ")
        self.exp=int(input("Enter the years of experience: "))

    def print_details(self):
        print("Name is ",self.name)
        print("Age is ",self.age)
        print("Gender is ",self.age)
        print("Subject taken is ",self.subject)
        print("Years of experience is ",self.exp)

teacher=Teacher("",0,"","",0)
teacher.get_details()
teacher.print_details()