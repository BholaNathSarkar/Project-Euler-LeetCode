for c in range(1,500):
    for b in range(1,c):
        for a in range(1,b):
            if(a+b+c==1000):
                p1=a**2+b**2
                if(p1==c**2):
                  print(a*b*c)
     
