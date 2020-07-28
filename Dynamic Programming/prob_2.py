""""
Problem:
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. Write a program to find Nth Ugly Number.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. For each testcase there is one line of input that contains the number N.

Output:
Print the Nth Ugly Number.

Constraints:
1 ≤ T ≤ 104
1 ≤ N ≤ 104

Example:
Input:
2
10
4
Output:
12
4

"""

##CODE

ugly = [0]*10001
ugly[0] = 1
i2=i3=i5=0
n2=2
n3=3
n5=5
for i in range(1,10001):
    ugly[i] = min(n2,n3,n5)

    if(ugly[i] == n2):
        i2 += 1
        n2 = ugly[i2] * 2

    if(ugly[i] == n3):
        i3 += 1
        n3 = ugly[i3] * 3

    if(ugly[i] == n5):
        i5 += 1
        n5 = ugly[i5] * 5

t = int(input())
while(t!=0):
    n = int(input())
    print(ugly[n-1])
    t -= 1
