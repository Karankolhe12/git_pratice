class a():
     def kk (self):
         print("ram a")
     
class b(a):
     def kk (self):
         print("ram b")
class c(a):
   def kk (self):
         print("ram c")
class d(c,b):
   def kk (self):
         print("ram d")

A=a()
B=b()
C=c()
D=d()
D.kk()