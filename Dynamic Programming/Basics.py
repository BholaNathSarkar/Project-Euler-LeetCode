
#Fibonacci using Recursion
def fib(n):
    if(n<2):
        return 1
    return fib(n-1) + fib(n-2)
print(fib(5))

#Using Dp Memoization
def fib (n):
    f = [0] * n
    f[0] = 0
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f
print(fib(10))



### SAMPLE PROBLEM ###
"""
Let us say that you are given a number N, you've to find the number of different ways to write it as the sum of 1, 3 and 4.
   For example, if N = 5, the answer would be 6.
                1 + 1 + 1 + 1 + 1
                1 + 4
                4 + 1
                1 + 1 + 3
                1 + 3 + 1
                3 + 1 + 1
Sub-problem: DPn be the number of ways to write N as the sum of 1, 3, and 4.
Finding recurrence: Consider one possible solution, n = x1 + x2 + ... xn. If the last number is 1, the sum of the remaining numbers should be n - 1.
So, number of sums that end with 1 is equal to DPn-1..
Take other cases into account where the last number is 3 and 4. The final recurrence would be:

                            DPn = DPn-1 + DPn-3 + DPn-4.

Take care of the base cases. DP0 = DP1 = DP2 = 1, and DP3 = 2.

"""
def dp_sample(n):
    DP = [0] * 10000
    DP[0] = DP[1] = DP[2] = 1
    DP[3] = 2 ## 3 = 1 + 1 + 1, 3 = 3
    for i in range(4, n+1):
        DP[i] = DP[i-1] + DP[i-3] + DP[i-4]
    return DP[n]

print(dp_sample(5))


#### Sample 2 ###
"""
Given an integer N, print the factorial of the N (mod ).
Input:
First line contains one integer, T, number of test cases.
Each test case contains one integer, N.
Output:
For each test case you need to print the factorial of N (mod ).
Constraints:
1<= T <= 10^5
0 <= N <= 10^5
"""

#Code:
m = 1000000007
num = 100001  #range of N in constraint
fact= [0] * num
fact[0] = 1
for i in range(1,num):
    fact[i] = (i * fact[i-1]) % m
t = int(input())
while(t>0):
    n = int(input())
    print(fact[n])
    t -=1
