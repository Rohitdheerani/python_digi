from tkinter import W


class Shape:

    def__init__(self,side):
        self.side = side

    def info(self):
        return f'shape with{self.side}'

class Rectangle(shape):

    def__init__(self,1,w):
         super().__init__(1)
         self.w = W

   def area(self):
       return self,side*self.w#side is taken AS Length

    # overidden function
    def info(self):
        return 'rectangle with 1 = {self.side} & w ={self.w}'

ob1 = shape(4)
print (ob1.info())
print(ob2.info())
                   