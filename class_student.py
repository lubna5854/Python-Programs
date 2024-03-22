
class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def get_details(self):
        self.name=input("Enter your name :")
        self.mark=int(input("Enter your mark: "))
    def put_details(self):
        print(self.name,self.mark)

obj=student('','')
obj.get_details()
obj.put_details()
