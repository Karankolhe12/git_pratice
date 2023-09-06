# k=[2,5,2,7,8,9]
# x 
def s(x):
    return x*x
def t(x):
    return x*x*x
p=[s,t]
for i in range(9 ):
   l=list(map(lambda x:x(i),p))
   print(l)
