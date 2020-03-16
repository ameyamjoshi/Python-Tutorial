n=int(input())
a = list(map(int,input().strip().split()))[:n] 
max = 0
res = a[0] 
for i in a: 
    freq = a.count(i) 
    if freq > max: 
        max = freq 
        res = i 

print(max)

