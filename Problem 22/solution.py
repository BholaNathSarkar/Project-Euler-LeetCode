names=sorted(open('p022_names.txt').read().rstrip().replace('"','').split(','))

score=lambda word:sum(ord(c)-64 for c in word)   ##ASCII of ‘A’ is 65, ‘B’ is 66, …, and ‘Z’ is 90
#so we subtract 64 from the ASCII value to normalize the range

val=sum(count*score(name) for count,name in enumerate(names,start=1))

print("Total Score: ",val)
