for i in range(25,50):
    if i>1:
      for j in range(2,i):
        if(i % j)==0:
            break
      else:
            print(i)