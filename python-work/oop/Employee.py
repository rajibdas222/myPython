class employee():
    def __init__(self,name,age,id,salary): #create a function
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id


emp1 = employee("Rajib",26,22,2000)        
emp2 = employee("Rajib22",28,28,4000)
print(emp1.age, emp2.salary)        
        