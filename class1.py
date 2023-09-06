class karan:
    k=34
    pass
    def s(self):
        return f"the name is {self.name} and the job is {self.job} and the role is {self.role} "
    @classmethod
    def h(cls,new_k):
        cls.k=new_k
        print(new_k)
    @staticmethod
    def j(str):
        print("this snake game is taken to compliate my hole  night " +str)   
        
p=karan()
p.name="ram"
p.job="student"
p.role="study"

# print(p.k)
# print(p.s())
# print(p.j("tis is fucking hard to explain"))
class kolhe(karan):
    no_of_holiday=56
    pass  
    def ko(self):
        return f"the name is {self.name} and the job is {self.job} and the role is {self.role} "
    @classmethod
    def hol(cls,new_holiday):
        cls.no_of_holiday=new_holiday
        print(f"{new_holiday}  day remain for my holidays")
    @staticmethod
    def stk(kp):
        return "what is your name baby "+kp  
s=kolhe()
s.name="patil"
s.job="student"
s.role="work"
print(s.stk("my name is moni"))
s.no_of_holiday=67
print(s.no_of_holiday,"day remain for my holidays")
print(p.s())
print (s.ko()) 
  
 

