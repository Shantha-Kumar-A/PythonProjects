#creating Parent class Company
class Company:

    def __init__(self, name, proj):
        self.name = name #public attribute
        self._proj = proj #protected attribute

        
    
#creating child class Emp
class Emp(Company):


    def __init__(self, eName, sal, cName, proj):
        
        #calling the constructor
        Company.__init__(self, cName ,proj)
        self.name = eName #public attribute
        self.__sal = sal  #private attribute

  #public func to shoe salary details
    def show_sal(self):
        print("the salary Of ",self.name," is:   ",self.__sal,)

#creating instance of Company class
c = Company("Future_Focus","Accounts")
#creating instance of Emp class
e = Emp("Henry", 5000, c.name, c._proj)

print("Welcome to ",c.name)
print("Here ",e.name,"is working on ",e._proj)


e.show_sal()
