sum=5
n=2000000
for i in range(3,n,2):
    j=1
    while(j*j<i):
      j+= 2
      if(i%j==0):
         break
    else:
        sum+=i
print(sum)
