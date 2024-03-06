class Robot:
    population = 0
    def __init__(self, name):
        self.name = name
        print("Initialization {0}".format(self.name))
        Robot.population +=1

#garbage collector deletes variables that are not used
#opposite to constructor __init__ - destructor method delete __del__        
        
    # def __del__(self):
    def destroy(self):
        print(f"{self.name} destroyed")
        # dont forget to add f""
        Robot.population -=1
        if Robot.population == 0:
            print(f"{self.name} was last")
        else:
            print("{0} robots remain".format(Robot.population)) 
               
    def say_hi(self):
        print("Hello! My name is {0}".format(self.name))
    
    def how_many():
        print("This planet has {0} robots".format(Robot.population))

# formats will be used for jango projects on second course

droid1 = Robot("R2-D2")
Robot.how_many()
droid2 = Robot("C-3PO")
Robot.how_many()

Robot.destroy(droid1)

# del droid1
# del droid2

# print(Robot.__doc__)