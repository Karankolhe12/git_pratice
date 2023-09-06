class a:
    p=56
    pass
    
    def karan (self):
        print( f"my name is {self.name} and i did my garduvation in the fied of {self.field} ")
    @classmethod
    def sk(cls,q):
        cls.p=q
        print(q)
    @staticmethod
    def stk(any):
        print("this is my laptop and my laptop wallpepper is jay shree ram "+any)
       
kk=a()
kk.name="karan kolhe"    
kk.field="bsc chemistry"
kk.p="karan is my name and i am student and i am doing the course master in computer science"
print(kk.stk("ram ram ki raja ram"))
print(kk.p)
print(kk.karan())