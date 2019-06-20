max=0
val=0
#count=0
for n in range(1,1000000):
    count=0
    p=n
    while(n>1):
        count+=1
        if(n%2==0):
            count+=1
            n=n/2
        else:
             n=3*n+1
    if(count>max):
        max=count
        val=p
print(val)
