def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def combination(n):
    x=2*n
    y=n
    return fact(x)/(fact(y)*fact(y))  ##2nCn means choosing n(right moves) moves from total 2n moves
##as half of the moves should always be right move and other half is down move
print(combination(20))
