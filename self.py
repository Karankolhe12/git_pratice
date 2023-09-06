class karan:
    number=23
    pass
    def k(self):
        return f"oo your name is {self.name}"
    @classmethod
    def s (cls,new_number):
      cls.number=new_number
    # print(number)
    @staticmethod
    def s(str):
        print( "this is for you "+str)
    
p=karan()
p.name="karan" 
p.s("kk")
p.number=56
print(p.number)
print(p.k())       