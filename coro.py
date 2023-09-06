def k ():
    import time
    k=[1,4,7,6,4]
    # print(k)
    time.sleep(2)
    while True:
        # p=int(input("enter the word : "))
        text=(yield)
        if text in k:
            print("your text in book")
        else:
            print("your  is not in book")
            

ka=k()
print("searched started")
next(ka)
p=int(input("enter the word : "))

ka.send(p)
print("next method run")        
ka.send("k4") 
ka.send("itom20")
