import math
sum=0
n=100
for i in range(1,n):
    sum+=i
    #print(sum)
    count=0          #for taking consider 1 as a factor
    for j in range(1, int(math.ceil(math.sqrt(sum)))):
        ##print(sum)
        if(sum%j==0):
            count+=2

    if(count>=30):
        print(sum)
        break
    n+=1
##print(sum)
