'''



class Calculator:

    def __init__(self,name):
        print(f'welcom {name}')

    def sum(self,x,y):
        print(x+y)


    def mul(self,x,y):
        print(x*y)




class SciCalculator(Calculator):
    def power(self,x,y):
        print(x**y)

b=Calculator('shereen')
b.sum(2,3)

        
s1=SciCalculator('yazan')
print(SciCalculator.mro())
s1.mul(2,2)



class A:
    def do(self):
        print('A')

class B:
    pass

class C:
    def do(self):
        print('c')

class D(C,B):
    pass

o1=D()
print(D.mro())
'''

class Student:
    
    global marks
    marks=[1,2]
    


    def __init__(self):
        
        self.marks=[]


    def print_marks(self):
        print(marks)

    

s=Student()
s.print_marks()


















