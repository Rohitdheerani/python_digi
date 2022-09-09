class Fruits:
    color = 'red'
    taste = 'sweet'

class veg:
    size = 'small'
    age = 'fresh'

class GM(Fruits,veg):
    name = 'GM-122'

g = GM()             

print(g.name)
print(g.color)
print(g.taste)
print(g.size)
print(g.age)



#2



class Calculation1:
    def Summation(self,a,b):
     return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))
               
