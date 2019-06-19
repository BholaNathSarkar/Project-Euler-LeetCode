lp=0
n=600851475143
count=0
i=2
##for i in range(1,n):
while(i*i<=n):
    if(n%i==0):
        count=1
        for j in range(2,i):  ##check whether i is prime factor
            if(i%j==0):
                count=0
        if(count==1):
            lp=i             ##assigning i to lp, lp is overwriiten everytime we get a larger prime factor
    i+=1
print(lp) 
