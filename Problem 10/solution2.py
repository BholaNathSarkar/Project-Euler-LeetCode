import math
sum=0
n=2000000
for i in range(2,n):
   for j in range(2,int(math.sqrt(i)) + 1):
       if(i%j==0):
               break
   else:
           sum+=i
print(sum)
