''' Using the concept of object oriented programming and inheritance,
create a super class named vehicles, which has two sub classes
 named car and bike. Define two methods in the vehicles class
 named getspecs and displayspecs, to get the specifications and
 display the specifications of the vehicles. You can use any
 specifications which you want. The car class and the bike class
 should have one specification which is exclusive to them for
 example wheels can have marks as a special specification. Make
 sure that the sub classes have their own methods to get and display
 their special specification. Create an object of car/ bike and make
 sure to call all the methods from the vehicle class as well as the
 methods from the own class.'''

class vehicles:
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color
    def get_specs(self):
        print("details of the vehicle: ")
        self.model=input("model: ")
        self.year=input("Year: ")
        self.color=input("Color: ")

    def display_specs(self):
        print("The specifications of the vehicle :")
        print("Model: ",self.model)
        print("Year: ",self.year)
        print("Color: ",self.color)

class car(vehicles):
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color

class bike(vehicles):
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color

#object creation
c=car('','','')
c.get_specs()
c.display_specs()
b=bike('','','')
b.get_specs()
b.display_specs()




