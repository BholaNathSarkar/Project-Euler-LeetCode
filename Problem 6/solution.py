def sum_square_difference(n):
 sum1=n*(n+1)/2
 result1=sum1**2
 result2=0
 for i in range(1,n+1):
    result2+=i**2
 diff=result1-result2
 return diff

print(sum_square_difference(100))
