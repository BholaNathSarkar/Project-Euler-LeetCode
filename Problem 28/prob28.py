sum=0
i=3
term=2
count=0
while(i<(1001**2+1)):    ##for 1001 by 1001 spiral range of numbers will be (1,1001*1001 +1)
    sum+=i
    count+=1
## we see the diagonal sum is happening as [1,3,5,7,9,13,17,21,25,31,37,43,49,57,65,73,81, .....]
##if we see from number 3, then the number is increasing by 2  upto 4th count i.e 9 ,after that it is increasing at a rate of 4 again upto 4th count i.e 25
##and after that it increasing at a rate of 6 till 49 and so on
    if(count%4==0):
        term+=2
        i+=term
    else:
        i+=term
print(sum+1)  ##remaining 1 is added here as he start i from 3
