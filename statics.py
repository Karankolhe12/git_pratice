class patil:
    number=56
    pass
    def pk(self): 
     return (f"this is my name {self.name}")
    @classmethod
    def stk(cls,newnumber):
        cls.number=newnumber
    @staticmethod
    def po(str):
        print("this is good " +str)

        
pp=patil()
pp.name="kolhe"
pp.snumber=45
pp.po("for making some noney")   
print(pp.pk())