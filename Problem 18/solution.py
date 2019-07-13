table=[[int(n) for n in s.split()] for s in open("numbers.txt").readlines()]  ##reads the data and form the array table
for row in range(len(table)-1,0,-1):
    for col in range(0, row):
        table[row-1][col]+=max(table[row][col], table[row][col+1])
print("Maximum total is",table[0][0])
