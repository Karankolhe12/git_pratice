class mi:
    kp="jay shree ram"
    pass
    def __init__(self,anem,ajob,arole,sala):
       self.name=anem
       self.job=ajob
       self.role=arole
       self.salary=sala
    def sk(self):
      return f"the name of the student is {self.name} and he oh doing {self.job} and he is {self.role} and the ssalary is{self.salary}"
    @classmethod
    def ks(cls,ram):
        cls.kp=ram
        print(ram)     
    def __add__(self,other):
      return self.salary + other.salary
    def __truediv__(self,other):
      return self.salary / other.salary
      
      
    

kk=mi("kara","nothing","nothing",2500)
kp=mi("patil","master","teaching",500)
print(kk.sk())
print(kp.sk())
kk.kp="ram ram ki raja ram"
print(kk+kp)
print(kk/kp)

print(kk.kp)


