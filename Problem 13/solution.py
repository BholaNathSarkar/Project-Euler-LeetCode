numbers = []

with open("digit.txt",'r') as f:
    for num in f:
        numbers.append(int(num))

print(str(sum(numbers))[:10])
