def nth_prime(n):

  count=2
  for i in range(3,n**2,2):
    j=1
    while(j*j<i):
      j+= 2
      if(i%j==0):
         break
    else:
        count+=1
    if(count==n):
        return i

print (nth_prime(10001))
