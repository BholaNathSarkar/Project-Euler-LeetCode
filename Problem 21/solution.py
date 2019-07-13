##This is not an optimized solution ,it tooks around 10-15 secdond to compile
amicable_sum=0
for i in  range(1,10000):
    j=1
    sum=0
    while(j<i):
        if(i%j==0):
            sum+=j
            j+=1
        else:
            j+=1
    k=1
    sum2=0
    while(k<sum):
        if(sum%k==0):
            sum2+=k
            k+=1
        else:
            k+=1
    if(sum2==i and i!=sum):
        amicable_sum+=(i+sum)
print("Final answer",amicable_sum/2)   ##dividing by 2,as we will be getting same number two times,for example we will get get 284 from 220 and again we will get 220 from 284
