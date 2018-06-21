#q2  What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
#print a.f(), b.f() 
#print a.g(), b.g() 

#this will give syntax error ..we need to place brackets after print.

#correct code=
print (a.f(), b.f()) 
print (a.g(), b.g())

# Actual output= A B
#		 		 A B