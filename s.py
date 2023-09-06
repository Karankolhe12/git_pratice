apple=int(input("enter the number o apple : "))
mx=int(input("enter the maximum number of apple : "))
mn=int(input("enter the minimum number of apple : "))
for i in range(mn,mx):
    if apple%i==0:
        print(f"{i} is the divioser of {apple}")
    else:
         print(f"{i} is the not divioser of {apple}")
if apple is not int:
    print("plz enter the integer values")