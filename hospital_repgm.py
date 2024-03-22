# class hospital that accepts hospital details
class hospital:
    def __init__(self,admin,doctor,sister,dept):
        self.admin=admin
        self.doctor=doctor
        self.sister=sister
        self.dept=dept

    def get_details(self):
        self.admin=input("Admin name: ")
        self.doctor=input("Doctor name: ")
        self.sister=input("Sister name: ")
        self.dept=input("Department: ")
class patient(hospital):
    def __init__(self,name,age,doc,disease,contact):
        self.name=name
        self.age=age
        self.doc=doc
        self.disease=disease
        self.contact=contact
    def get_patient(self):
        self.name= input("Patient name: ")
        self.age=int(input("Patient age: "))
        self.doc=input("Doctor name: ")
        self.disease=input("Disease: ")
        self.contact=int(input("Contact number: "))
class department(patient):
    def __init__(self,admin,doctor,sister,dept,name,age,doc,disease,contact):
        self.admin = admin
        self.doctor = doctor
        self.sister = sister
        self.dept = dept

        self.name=name
        self.age=age
        self.doc=doc
        self.disease=disease
        self.contact=contact
    def display(self):
        print("The hospital details: ")
        print("Admin name: ",self.admin)
        print("Doctor name: ",self.doctor)
        print("Sister name: ", self.sister)
        print("Department name: ",self.dept)
    def disp_patient(self):
        print("Patient name: ", self.name)
        print("Patient age: ",self.age)
        print("consulting doctor: ",self.doc)
        print("Disease diagnosed: ",self.disease)
        print("Contact details: ",self.contact)

d=department('','','','','','','','','')
d.get_details()
d.get_patient()
d.display()
d.disp_patient()
