def powerofTwo(n):
    value=1
    while(n>0):
       value=2*value
       n=n-1
    return value


def sum_of_digits(n):
    sum=0
    a=0
    while(n>0):
       a=n%10
       sum+=a
       n=n//10
    return sum

num=powerofTwo(1000)
print(sum_of_digits(num))
